# Create split_scale.py that will contain the functions that follow.
# Each scaler function should create the object, fit and transform both train and test.
# They should return the scaler, train dataframe scaled, test dataframe scaled.
# Be sure your indices represent the original indices from train/test, as those represent the indices from the original dataframe.
# Be sure to set a random state where applicable for reproducibility!

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

import wrangle
import env

from sklearn.model_selection import train_test_split

def split_to_scale(dataframe):
    return train_data, test_data = train_test_split(dataframe, train_size = 0.8, random_state = 123)

def split_my_data(X, y, train_pct):
    return X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

def standard_scaler(train_data, test_data):
    # Creates a Standard Scaler object and fit Train Data 
    standard_scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train_data)
    # Scale Train Data and Convert to a Data Frame
    scaled_train = standard_scaler.transform(train_data)
    scaled_train = pd.DataFrame(scaled_train, columns=train_data.columns).set_index([train_data.index])
    # Scale Train and Convert to a Data Frame
    scaled_test = standard_scaler.transform(test_data)
    scaled_test = pd.DataFrame(scaled_test, columns=test_data.columns).set_index([test_data.index])
    return scaled_train, scaled_test, standard_scaler

def scale_inverse(scaled_train_data, scaled_test_data):
    unscaled_train_data = standard_scaler.inverse_transform(scaled_train_data)
    unscaled_test_data = standard_scaler.inverse_transform(scaled_test_data)

def uniform_scaler(train_data, test_data):
    # Creates a Uniform Scaler object and fit Train Data 
    uniform_scaler = QuantileTransformer(n_quantiles=100, output_distribution="uniform", random_state=123, copy=True).fit(train_data)
    # Scale Train Data and Convert to a Data Frame
    scaled_train = uniform_scaler.transform(train_data)
    scaled_train = pd.DataFrame(scaled_train, columns=train_data.columns).set_index([train_data.index])
    # Scale Train and Convert to a Data Frame
    scaled_test = uniform_scaler.transform(test_data)
    scaled_test = pd.DataFrame(scaled_test, columns=test_data.columns).set_index([test_data.index])
    return scaled_train, scaled_test, uniform_scaler

def gaussian_scaler(train_data, test_data):
    # Creates a Gaussian Scaler object and fit Train Data 
    gaussian_scaler = PowerTransformer(method="yeo-johnson", standardize=False, copy=True).fit(train_data)
    # Scale Train Data and Convert to a Data Frame
    scaled_train = gaussian_scaler.transform(train_data)
    scaled_train = pd.DataFrame(scaled_train, columns=train_data.columns).set_index([train_data.index])
    # Scale Train and Convert to a Data Frame
    scaled_test = uniform_scaler.transform(test_data)
    scaled_test = pd.DataFrame(scaled_test, columns=test_data.columns).set_index([test_data.index])
    return scaled_train, scaled_test, gaussian_scaler

def min_max_scaler(train_data, test_data):
    # Creates a Min-Max Scaler object and fit Train Data 
    minmax_scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train_data)
    # Scale Train Data and Convert to a Data Frame
    scaled_train = minmax_scaler.transform(train_data)
    scaled_train = pd.DataFrame(scaled_train, columns=train_data.columns).set_index([train_data.index])
    # Scale Train and Convert to a Data Frame
    scaled_test = uniform_scaler.transform(test_data)
    scaled_test = pd.DataFrame(scaled_test, columns=test_data.columns).set_index([test_data.index])
    return scaled_train, scaled_test, min_max_scaler

def iqr_robust_scaler(train_data, test_data):
    # Creates a Robust Scaler object and fit Train Data 
    robust_scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(train_data)
    # Scale Train Data and Convert to a Data Frame
    scaled_train = minmax_scaler.transform(train_data)
    scaled_train = pd.DataFrame(scaled_train, columns=train_data.columns).set_index([train_data.index])
    # Scale Train and Convert to a Data Frame
    scaled_test = uniform_scaler.transform(test_data)
    scaled_test = pd.DataFrame(scaled_test, columns=test_data.columns).set_index([test_data.index])
    return scaled_train, scaled_test, robust_scaler

