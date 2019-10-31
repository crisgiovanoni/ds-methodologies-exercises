# Fit the logistic regression classifier to your training sample
# and transform, i.e. make predictions on the training sample

from sklearn.linear_model import LogisticRegression
from acquire import get_iris_data
from split_scale import split_my_data

df = get_iris_data()
df.head()

X = df[["sepal_length","sepal_width","petal_length","petal_width"]]
y = df[["species_name"]]

X_train, X_test, y_train, y_test = split_my_data(X,y,0.7)

log_model = LogisticRegression(C=1, random_state = 123, solver='saga').fit(X_train, y_train)
y_train_pred = log_model.predict(X_train)

y_train_pred = pd.DataFrame(y_train_pred).set_index=y_train
y_train_pred