#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from datetime import timedelta

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import DBSCAN

import warnings
warnings.filterwarnings("ignore")


# In[18]:


df = pd.read_csv("anonymized-curriculum-access.txt", sep=" ", header=None)
df["timestamp"] = df[0] + " " + df[1]

df.timestamp = pd.to_datetime(df.timestamp, infer_datetime_format=True)
df = df.drop(columns=[0,1])


# In[19]:


df[["url","id_ind","id_group","ip"]] = df[[2,3,4,5]]
df.drop(columns=df[[2,3,4,5]],inplace=True)


# In[20]:


df.id_group = df.id_group.fillna(0)
df.id_group = df.id_group.astype("int")


# In[21]:


df.head()


# In[22]:


df.groupby("id_group").count()


# 1. Compute every time stamp from beginning using time delta
# 2. Convert time delta into a float

# ### Select Features

# In[23]:


dfc = df[["timestamp","id_ind"]]


# In[24]:


dfc["timedelta"] = dfc.timestamp - dfc.timestamp[0]


# In[25]:


dfc["timefloat"] = dfc.timedelta.dt.total_seconds()


# In[26]:


dfc.head()


# In[27]:


dfc.drop(columns=["timestamp","timedelta"],inplace=True)


# In[28]:


dfc.head()


# ### Convert to float and np.array

# In[29]:


dfc_array = dfc.values.astype("float32", copy=False)


# In[30]:


dfc_array


# ### Scale

# In[31]:


scaler = MinMaxScaler().fit(dfc_array)
array_scaled = scaler.transform(dfc_array)


# ### DBSCAN 

# In[ ]:





# In[ ]:





# In[ ]:


dbsc = DBSCAN(eps= .75, min_samples = 15).fit(array_scaled)


# In[ ]:




