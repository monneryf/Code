import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from sklearn import datasets
from sklearn.linear_model import LogisticRegression

from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA
from sklearn.decomposition import KernelPCA

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

#####################################################################################
##########     DATA                     #############################################
#####################################################################################

W2 = V.T[:, :2]
X2D = X_centered.dot(W2)

pca = PCA(n_components = 2)
X2D = pca.fit_transform(X)

print(pca.explained_variance_ratio_)

#####################################################################################

pca = PCA()
pca.fit(X_train)
cumsum = np.cumsum(pca.explained_variance_ratio_)
d = np.argmax(cumsum >= 0.95) + 1

pca = PCA(n_components=0.95)
X_reduced = pca.fit_transform(X_train)

#####################################################################################

pca = PCA(n_components = 154)
X_reduced = pca.fit_transform(X_train)
X_recovered = pca.inverse_transform(X_reduced)

#####################################################################################

n_batches = 100

inc_pca = IncrementalPCA(n_components=154)
for X_batch in np.array_split(X_train, n_batches):
    inc_pca.partial_fit(X_batch)

X_reduced = inc_pca.transform(X_train)

#####################################################################################

X_mm = np.memmap(filename, dtype="float32", mode="readonly", shape=(m, n))

batch_size = m // n_batches
inc_pca = IncrementalPCA(n_components=154, batch_size=batch_size)
inc_pca.fit(X_mm)

#####################################################################################

rnd_pca = PCA(n_components=154, 
              svd_solver="randomized")

X_reduced = rnd_pca.fit_transform(X_train)

#####################################################################################

rbf_pca = KernelPCA(n_components = 2, 
                    kernel="rbf", 
                    gamma=0.04)

X_reduced = rbf_pca.fit_transform(X)

#####################################################################################

clf = Pipeline([
        ("kpca", KernelPCA(n_components=2)),
        ("log_reg", LogisticRegression())
    ])

param_grid = [{
        "kpca__gamma": np.linspace(0.03, 0.05, 10),
        "kpca__kernel": ["rbf", "sigmoid"]
    }]

grid_search = GridSearchCV(clf, 
                           param_grid, 
                           cv=3)

grid_search.fit(X, y)

print(grid_search.best_params_)






