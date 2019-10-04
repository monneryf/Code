import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#####################################################################################
##########     DATA                     #############################################
#####################################################################################


X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]  # add x0 = 1 to each instance
y_b = 4 + 3* X_b + np.random.rand(100,1)
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

#####################################################################################
##########     VISUALISATION          ###############################################
#####################################################################################

#print(X_b)
#print(y_b)
#print(theta_best)

#plt.scatter(x=X,
#            y=y)

#####################################################################################
##########     MACHINE LEARNIG          #############################################
#####################################################################################

lr = LinearRegression()
lr.fit(X,y)

predictions = lr.intercept_ + X * lr.coef_

#plt.plot(X,
#        predictions,
#        c='red')

#####################################################################################

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

lr.fit(X_poly,y)

predictions = lr.intercept_ + X_poly.dot(lr.coef_.T)

print(X[0])
print(X_poly[0])
print([lr.intercept_,lr.coef_])
print(predictions[0])

plt.scatter(x=X,
            y=predictions,
            c='green')

plt.show()




