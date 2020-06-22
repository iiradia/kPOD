# imports for mathematical functions
import numpy as np
from numpy import nanmean, nan
import sys
from scipy.spatial import distance
import pandas as pd

# import helper methods
from ..utils.initial_helpers import __initialize
from ..utils.utils import (
    __check_convergence, 
    __cluster_assignment, 
    __fill_data, 
    __move_centroids
)

def k_pod(data, n_clusters,max_iter=300,tol=0):
    """ Compute cluster centers and predict cluster index for sample containing missing data.

    Parameters
    ----------
    data: {array-like, sparse matrix} of shape (N, P)
        Data to predict clusters for.

    n_clusters: int
        The number of clusters to choose
    
    max_iter: int
        Maximum number of iterations to be run, default 300.

    tol: float
        Tolerance level for movement in cluster centroids, default 0.

    Returns 
    -------
    labels: ndarray of shape (N,)
        Index of the cluster each sample belongs to.

    """
    # convert data to numpy array
    data = np.array(data)
    
    # assign initial variables
    N = data.shape[0]
    P = data.shape[1]
    K = n_clusters
    num_iters = 0   

    # collect missing indiices
    MISSING_DATA = data.copy()

    # initialize past centroids
    past_centroids = []
    cluster_centers = []
    cluster_assignment = []

    # loop through max iterations of kPOD
    while num_iters < max_iter:

        """
        STEP 1: Imputation of missing values
        fill with the mean of the cluster (centroid)
        """

        # if it has been multiple iterations, fill with algorithm
        if num_iters > 0:

            # fill data after first iteration
            filled_data = __fill_data(MISSING_DATA, cluster_centers, cluster_assignment)

            # save data as np array
            filled_data = np.array(filled_data)

        # fill with initial imputation if first iteration 
        else:

            # initial imputation
            data_frame = pd.DataFrame(data)
            filled_data = np.array(data_frame.fillna(nanmean(data)))

            # initialize cluster centers so other methods work properly
            cluster_centers = __initialize(filled_data, K)
        
        """
        STEP 2: K-Means Iteration
        """

        # Cluster Assignment
        cluster_assignment = __cluster_assignment(filled_data, cluster_centers, N, K)

        # Move centroids
        cluster_centers = __move_centroids(filled_data, cluster_centers, cluster_assignment, N, K)
        
        """
        STEP 3: Check for convergence
        """

        # check for convergence of algorithm
        centroids_complete = __check_convergence(cluster_centers, past_centroids, tol, num_iters)  

        # set past centroids to current centroids  
        past_centroids = cluster_centers

        # increase counter of iterations
        num_iters += 1

        # if k means is complete, end algo
        if (centroids_complete):
            break

    # return assignments and centroids
    cluster_ret = {"ClusterAssignment" : cluster_assignment, "ClusterCenters" : cluster_centers}
    
    cluster_return  = (cluster_assignment, cluster_centers)
    return cluster_return