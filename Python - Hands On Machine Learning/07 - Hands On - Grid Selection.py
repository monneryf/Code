import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import hashlib

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV

PATH = "E:\\Data\\Hands-on-Machine-Learning"
NAME_FILE = "housing_prepared.csv"

def importation_donnees(chemin,nom_fichier):
    file_name = os.path.join(chemin,nom_fichier)
    data = pd.read_csv(file_name)
    return data

#####################################################################################
##########     DATA                     #############################################
#####################################################################################

housing = importation_donnees(PATH,'housing.csv')

housing_prepared = importation_donnees(PATH,NAME_FILE)
housing_labels = importation_donnees(PATH,'housing_labels.csv')

housing_prepared_test = importation_donnees(PATH,'housing_prepared_test.csv')
housing_labels_test = importation_donnees(PATH,'housing_labels_test.csv')
label_test = np.asarray(housing_labels_test)

#####################################################################################
##########     MACHINE LEARNING          ############################################
#####################################################################################

param_grid = [
    {'n_estimators': [3, 10, 30], 
     'max_features': [2, 4, 6, 8]},
    {'bootstrap': [False], 
     'n_estimators': [3, 10], 
     'max_features': [2, 3, 4]},
  ]

forest = RandomForestRegressor()

grid_search = GridSearchCV(forest,
                           param_grid,
                           scoring="neg_mean_squared_error",
                           cv=5)

grid_search.fit(housing_prepared,
                housing_labels)


print(grid_search.best_params_)
print(grid_search.best_estimator_)

feature_importances = grid_search.best_estimator_.feature_importances_

extra_attribs = ["rooms_per_hhold", 
                 "pop_per_hhold", 
                 "bedrooms_per_room"]

cat_one_hot_attribs = list(encoder.classes_)
attributes = num_attribs + extra_attribs + cat_one_hot_attribs

sorted(zip(feature_importances, attributes), reverse=True)



