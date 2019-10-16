from sklearn.feature_selection import SelectKBest, f_regression

def select_kbest_freg_unscaled(X_train, y_train,k):
    """
    Takes X_train, y_train (scaled) and k as input, and
    Returns a list of the top k features
    """
    f_selector = SelectKBest(f_regression,k=k).fit(X_train,y_train)
    f_support = f_selector.get_support()
    f_features = list(X_train.columns[f_support])
    return f_features