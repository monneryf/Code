import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from numpy.linalg import inv
from numpy import dot, transpose

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = np.asarray([6, 8, 10, 14, 18]).reshape(-1,1)
y = np.asarray([7, 9, 13, 17.5, 18])

print(X.shape)
print(y.shape)

lr = LinearRegression()

lr.fit(X,y)

value_predict = np.asarray([13]).reshape(-1,1)

prediction = lr.predict(value_predict)

print(prediction)

X2 = np.asarray([[1, 6, 2], [1, 8, 1], [1, 10, 0], [1, 14, 2], [1, 18, 0]])

gauss_pivot = dot(inv(dot(transpose(X), X)), dot(transpose(X), y))

print(gauss_pivot)

xx = np.linspace(0,20,100).reshape(-1,1)
yy = lr.predict(xx)

plt.plot(xx,yy)

quadratic_feature = PolynomialFeatures(degree=2)
X_quad = quadratic_feature.fit_transform(X2)
xx_quad = quadratic_feature.fit_transform(xx.reshape(xx.shape[0],1))

reg = LinearRegression()
reg.fit(X_quad,y)

print(X_quad)
print(X_quad.shape)
print(xx_quad.shape)
print(xx_quad)

#xx_quad_pred = reg.predict(xx_quad)

#plt.plot(xx,xx_quad_pred,c='red',linestyle='--')

plt.title('Pizza price regressed on diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.axis([0, 25, 0, 25])
plt.grid(True)

plt.scatter(X,y)

plt.show()



