# imports for mathematical functions
import numpy as np
from numpy import nanmean, nan
import sys
from scipy.spatial import distance
import pandas as pd

def __cluster_assignment(data, cluster_centers, N, K):
    """ Assign each point in the dataset to a cluster based on its distance from cluster centers
    
    This is a helper method for the main kPOD functionality. It 
    executes the cluster assignment part of the algorithm.

    Parameters
    ----------
    data: {array-like, sparse matrix} of shape (N, P)
        Data to predict clusters for.

    cluster_centers: {array-like, sparse matrix} of shape (K,)
        Central point of each of the K clusters.

    N: int
        The number of observations in the data.
    
    K: int
        The number of clusters to assign centers for.

    Returns 
    -------
    cluster_assignment: ndarray of shape (N,)
        The cluster index that each data point was assigned to.
    """

    # set empty distance array with length of num clusters
    cluster_assignment = np.zeros(N)
    dist = np.zeros(K)

    # iterate through observations
    for num in range(0,N):

        # iterate through each cluster
        for cluster in range(K):

            # assign distance between point and cluster center
            dist[cluster] = distance.euclidean(data[num], cluster_centers[cluster])

        # assign point to cluster center with lowest distance
        cluster_assignment[num] = np.argmin(dist)

    # return the cluster assignments for this iteration
    return cluster_assignment

def __move_centroids(data, cluster_centers, cluster_assignment, N, K):
    """ Move each cluster centroid to the mean location of the points that are assigned to it.
    
    This is a helper method for the main kPOD functionality. It 
    executes the move cluster centroids part of the algorithm.

    Parameters
    ----------
    data: {array-like, sparse matrix} of shape (N, P)
        Data to predict clusters for.

    cluster_centers: {array-like, sparse matrix} of shape (K,)
        Central point of each of the K clusters.

    cluster_assignment: {array-like, sparse matrix} of shape (N,)
        Array containing the cluster index that each data point was assigned to.

    N: int
        The number of observations in the data.
    
    K: int
        The number of clusters to assign centers for.

    Returns 
    -------
    cluster_assignment: ndarray of shape (N,)
        The cluster index that each data point was assigned to.
    """

    # iterate through each cluster 
    for num in range(1, K+1):

        # make empty array cluster points
        cluster_points = list()

        # iterate through each data point
        for i in range(0, N):

            # if the cluster is assigned to this centroid, add it to the list of cluster points
            if int(cluster_assignment[i]) == (num-1):

                #  add data point to list of cluster points
                cluster_points.append(data[i])

        # convert the cluster points to an ndarray
        cluster_points = np.array(cluster_points)

        # set the new cluster centroid location to the main of the points it is assigned to
        cluster_centers[num-1] = cluster_points.mean(axis=0)
    
    # return moved cluster centers
    return cluster_centers

def __check_convergence(cluster_centers, past_centroids, tol, num_iters):
    """ Ensure that each cluster center is within the tolerance level of the last centroid.
    
    This is a helper method for the main kPOD functionality. It 
    executes the check convergence part of the algorithm.

    Parameters
    ----------
    cluster_centers: {array-like, sparse matrix} of shape (K,)
        Central point of each of the K clusters.

    past_centroids: {array-like, sparse matrix} of shape (K,)
        Array containing central points from the last kPOD iteration.

    tol: float
        The tolerance for each cluster center and its past centroid.
    
    num_iters: int
        Number of iterations of the algorithm.

    Returns 
    -------
    centroids_complete: boolean
        True if the cluster centers have converged, False otherwise.
    """

    # if it is the first iteration, algorithm has not converged
    if num_iters == 0:
        return False
    
    # set initial complete to 0
    centroids_complete = 0
    
    # check if k-means is complete
    for i in range(len(cluster_centers)):

        # if the distance between this centroid and the past centroid is less than tolerance
        if (distance.euclidean(cluster_centers[i], past_centroids[i]) <= tol):

            # add centroid to the list of complete centroids
            centroids_complete += 1

    # return list of centroids that have converged
    return centroids_complete

def __fill_data(MISSING_DATA, cluster_centers, cluster_assignment):
    """ Fill missing data with the average values for each data point's cluster.
    
    This is a helper method for the main kPOD functionality. It 
    executes the fill data part of the algorithm.

    Parameters
    ----------
    MISSING_DATA: {array-like, sparse matrix} of shape (N,P)
        Data with missing values.

    cluster_centers: {array-like, sparse matrix} of shape (K,)
        Central point of each of the K clusters.

    cluster_assignment: {array-like, sparse matrix} of shape (N,)
        Array containing the cluster index that each data point was assigned to.

    Returns 
    -------
    filled_data: {array-like, sparse matrix} of shape (N,P)
        Data with all nan values filled.
    """

    # save filled data as copy of missing data
    filled_data = np.array(MISSING_DATA.copy())

    # iterate through missing data
    for i in range(len(filled_data)):

        # set current cluster as cluster assignment of this data point
        obs_cluster = int(cluster_assignment[i])
        
        # reset counter to 0
        j = 0

        # iterate through each value
        for val in filled_data[i]:

            # if value is empty, replace it with cluster center value
            if (np.isnan(val)):

                # replace value with cluster center value (mean of its dimension)
                filled_data[i][j] = cluster_centers[obs_cluster][j]

            # increment counter
            j+=1
    
    # return data with all nan values filled 
    return filled_data