import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def label_encode(series):
    encode_toint = LabelEncoder()
    encode_toint.fit(series)
    series_arrayed = encode_toint.transform(series)
    return series_arrayed

def onehot_encode_labeled(one_d_array,list_of_column_names):
    # Reshape 1D array to 2D
    one_d_array = one_d_array.reshape(len(one_d_array),1)
    # Create, Fit_Transform
    ohe = OneHotEncoder(sparse=False, categories="auto")
    ohe_array = ohe.fit_transform(one_d_array)
    # Add labels to Array
    ohe_labels = list_of_column_names
    ohe_labeled_array = np.vstack((ohe_labels,ohe_array))
    return ohe_labeled_array

# >>> pd.DataFrame(data=data[1:,1:],    # values
# ...              index=data[1:,0],    # 1st column as index
# ...              columns=data[0,1:])

def split_data(df, train_ratio=0.8):
    # Use to split data into a train and test data with an 80-20 split
    train, test = train_test_split(df, train_size=train_ratio, random_state=123)
    return train, test