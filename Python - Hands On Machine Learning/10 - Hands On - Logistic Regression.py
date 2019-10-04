import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from sklearn import datasets
from sklearn.linear_model import LogisticRegression

#####################################################################################
##########     DATA                     #############################################
#####################################################################################

iris = datasets.load_iris()

list(iris.keys())

X = iris["data"][:, 3:]  # petal width
y = (iris["target"] == 2).astype(np.int)  # 1 if Iris-Virginica, else 0

#####################################################################################
##########     MACHINE LEARNIG          #############################################
#####################################################################################

log_reg = LogisticRegression()
log_reg.fit(X, y)

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_proba = log_reg.predict_proba(X_new)

#####################################################################################
##########     VISUALISATION          ###############################################
#####################################################################################

print(log_reg.predict([[1.7], [1.5]]))

plt.plot(X_new, y_proba[:, 1], "g-", label="Iris-Virginica")
plt.plot(X_new, y_proba[:, 0], "b--", label="Not Iris-Virginica")





