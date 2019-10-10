# Create split_scale.py that will contain the functions that follow.
# Each scaler function should create the object, fit and transform both train and test.
# They should return the scaler, train dataframe scaled, test dataframe scaled.
# Be sure your indices represent the original indices from train/test, as those represent the indices from the original dataframe.
# Be sure to set a random state where applicable for reproducibility!

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np

import wrangle
import env

# acquire data and remove null values 
df = wrangle.wrangle_telco()

# verify acquisition
df.info()

import pandas as pd
from sklearn.model_selection import train_test_split

train, test = train_test_split(df, train_size = .80, random_state = 123)


split_my_data(X, y, train_pct)
standard_scaler()
scale_inverse()
uniform_scaler()
gaussian_scaler()
min_max_scaler()
iqr_robust_scaler()