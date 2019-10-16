#### Feature Engineering for telco_churn data

import pandas as pd

from wrangle import wrangle_telco
from split_scale import split_my_data
import features

### SelectKBest - Top Features of Unscaled Data

## Step 1. Load Data
telco_df = wrangle.wrangle_telco()
telco_df.head()
telco_X = telco_df[["monthly_charges","tenure"]]
telco_y = telco_df["total_charges"]

## Step 2. Split Data to X and y, and test and train = 4 data frames
telco_X_train, telco_X_test, telco_y_train, telco_y_test = split_my_data(telco_X,telco_y, 0.80)

## Step 3. Run select_kbest_freg_unscaled
features.select_kbest_freg_unscaled(telco_X_train,telco_y_train,1)