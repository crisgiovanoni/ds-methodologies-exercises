from pydataset import data
faith=data('faithful', show_doc=True)
faith = data('faithful')

import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Exploration
r, pval = stats.pearsonr(faith.waiting, faith.eruptions)
print(f"Pearson's R = {r}")
sns.regplot(faith.eruptions,faith.waiting)

#Split Train-Test
x_train, x_test, y_train, y_test = train_test_split(faith.waiting, faith.eruptions, train_size=.70, random_state=123)

x_train = pd.DataFrame(x_train)
x_test = pd.DataFrame(x_test)
y_train = pd.DataFrame(y_train)
y_test = pd.DataFrame(y_test)

#Model
regmd = LinearRegression().fit(x_train, y_train)

score = regmd.score(x_train,y_train)
coeff = regmd.coef_
intercept = regmd.intercept_

yhat_train = pd.DataFrame(regmd.predict(x_train))

predictions = pd.DataFrame(y_train.copy())
predictions["yhat"] = yhat_train.copy()
predictions["waiting"] = x_train

#Visualization

predictions.plot.line(x="waiting", y="y_train")


Create a visualization with your predictions

waiting should be on the x axis, and eruptions on the y
Use color to differentiate the actual vs predicted values.
Add a descriptive title.
Change the y ticks such that they are all integers (i.e. no decimals)
Add the root mean squared error of your predictions as an annotation