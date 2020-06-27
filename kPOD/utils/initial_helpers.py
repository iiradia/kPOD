
# imports for mathematical functions
import numpy as np
from numpy import nanmean, nan
import sys
from scipy.spatial import distance
import pandas as pd

def __euclidean_distance(point_1, point_2):
    """ Computes euclidean distance given two points

    Parameters
    ----------
    point_1: float
        First point.
    
    point_2: float
        Second point.
    
    Returns
    -------
    euclidean_distance: float
        Euclidean distance between point_1 and point_2.
    """
    return np.sum((point_1 - point_2)**2)

def __initialize(data, n_clusters):
    """ Initialize cluster centers using k-means++ algorithm.

    Parameters
    ----------
    data: {array-like, sparse matrix} of shape (N, P)
        Data to predict clusters for.

    n_clusters: int
        The number of cluster centers to initialize.

    Returns 
    -------
    centroids: array of shape (n_clusters,)
        Coordinates for each cluster center.
    """
    # initialize 
    data = np.array(data)
    N = data.shape[0]

    # initialize the centroids list and add a randomly selected data point to the list
    centroids = []
    centroids.append(data[np.random.randint(N), :])

    # compute remaining k - 1 centroids
    for cluster in range(n_clusters - 1):

        # initialize a list to store distances of data points from nearest centroid
        distances = []
        
        for data_idx in range(N):

            # save current data point's coordinates
            point = data[data_idx, :]
            dist = sys.maxsize

            # loop through each centroid to find the minimum distances 
            for centroid_idx in range(len(centroids)):

                # compute distance of 'point' from each of the previously selected centroid and store the minimum distance
                curr_distance = __euclidean_distance(point, centroids[centroid_idx])
                dist = min(dist, curr_distance)
            
            # add distance to array
            distances.append(dist)

        # data point with max distance
        distances = np.array(distances)

        # add centroid to array and reset distances
        center = data[np.argmax(distances), :]
        centroids.append(center)
        distances = []

    # return array of centroids
    return centroids