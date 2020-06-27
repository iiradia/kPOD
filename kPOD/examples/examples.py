#imports for mathematical functions
import numpy as np
from numpy import nanmean, nan
import sys
from scipy.spatial import distance
import pandas as pd
import random
import matplotlib.pyplot as plt


def plot_data(p, data):
    """
    Function to create a scatterplot of data with more than 2 features.

    @param p number of features
    @param data dataset to be plotted
    """
    if (p > 2):
        pca = PCA(n_components = 2)
        pca.fit(data)

        new_data = pca.transform(data)
        x,y = new_data.T
        plt.scatter(x,y)

    else:
        x,y = data.T
        plt.scatter(x,y)
    
    
    plt.show()

def generate_complete_data(n, p, k, cluster_distance, mu = 0, sigma = 1, plot = False):
    """
    Function to generate n random numbers in a normal distribution.

    @param n =  number of observations
    @param p = number of features (dimensions)
    @param k = number of clusters
    @param cluster_distance = factor to create space between cluster centers
    @param mu = mean (default to standard normal)
    @param sigma = variance (default to standard normal)
    @param plot = False (determines whether or not to plot clusters)
    """

    # generates empty dataset with given shape
    data = np.zeros((n,p))

    # decides how to divide observations into clusters
    cluster_sep = n // k
    print(cluster_sep)
    mu_set = []

    # iterate through observations
    for obs in range(n):

        # modify mean to match current cluster center
        feature_mu = mu + (obs // cluster_sep)*cluster_distance
        
        # checks if the number of means is equal to number of clusters
        if len(mu_set) == k:

            # if so, set next mean to last mean
            feature_mu = mu_set[-1]

        # if mean is not in the set
        if feature_mu not in mu_set:

            # add mean to sets
            mu_set.append(feature_mu)

        # iterate through features/columns
        for feature in range(p):

            # add data point to each column
            data[obs][feature] = np.random.normal(feature_mu,sigma)


    # code to plot clusters of data
    if (plot == True):

        plot_data(p, data)
    
    # return created dataset
    return data


def generate_missing_indices(shape, missingness_pct):
    """
    Function to generate randomly separated missing data indices from given dataset.
    Returns numpy array consisting of missing data coordinates.

    @param shape = shape of dataset as a tuple of 2 values (n,p)
    @param missingness_pct = percentage of missing data to be generated
    """

    # list of missing indices
    missing_index_list = []

    # values for rows, obs, and missigness
    n = shape[0]
    p = shape[1]
    missingness = missingness_pct / 100

    # how many missing_indices to generate
    num_vals = n*p
    missing_vals = int(round(num_vals * missingness))

    # iterate through number of missing indices
    for i in range(missing_vals):

        # randomly generate missing indices
        random_n = random.randint(0, n-1)
        random_p = random.randint(0, p-1)

        # append tuple of index coordinates to list
        missing_index_list.append((random_n, random_p))

    # return missing indices
    return missing_index_list


def fill_missing_indices (data, missing_indices):
    """
    Function to fill dataset with missing values using given missing
    indices.

    @param data dataset to fill with missing values
    @param missing_indices indexes at which to place missing values --> tuple (x,y)
    """
    # create copy of current dataset
    new_data_set = data.copy()

    # iterate through number of missing_indices
    for coordinate in missing_indices:

        # calculate coordinates
        x = coordinate[0]
        y = coordinate[1]

        # fill value in dataset with NaN
        new_data_set[x][y] = np.NaN

    # return dataset containing missing values
    return new_data_set
