import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import hashlib

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix

def cartographie():
    housing.plot(kind="scatter",
                 x="longitude",
                 y="latitude",
                 alpha=0.4,
                 s=housing["population"]/100,
                 label="population",
                 figsize=(10,7),
                 c="median_house_value",
                 cmap=plt.get_cmap("jet"),
                 colorbar=True)

    plt.legend()
    plt.show()

def correlation():
    housing = train.copy()

    corr_matrix = housing.corr()
    facteurs = corr_matrix["median_house_value"].sort_values(ascending=False)
    print(facteurs)

    attributes = ["median_house_value", "median_income", "total_rooms",
                  "housing_median_age"]

    scatter_matrix(housing[attributes],figsize=(12,8))

    housing.plot(kind="scatter",
             x="median_house_value",
             y="median_income")

    plt.show()


