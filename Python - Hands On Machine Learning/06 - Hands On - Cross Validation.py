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

PATH = "E:\\Data\\Hands-on-Machine-Learning"
NAME_FILE = "housing_prepared.csv"

def importation_donnees(chemin,nom_fichier):
    file_name = os.path.join(chemin,nom_fichier)
    data = pd.read_csv(file_name)
    return data

def calcul_score(data,pred):
    errors = np.mean((data - pred )**2)
    errors_square = errors**(1/2)

    print('Erreur de prédictions Manual : {}'.format(errors_square))

    mean_square = np.sqrt(mean_squared_error(data,pred))
    print('Erreur de prédictions MSE : {}'.format(mean_square))

def display_score(score):
    print("Scores : ",score)
    print("Mean : ",score.mean())
    print("Standard deviation : ",score.std())

def validation_score(noyau):
    scores = cross_val_score(noyau,
                             housing_prepared,
                             housing_labels,
                             scoring="neg_mean_squared_error",
                             cv=10)

    display_score(np.sqrt(-scores))

def sauvegarde_modele(name,model):
    path_name = os.path.join(PATH,name)
    joblib.dump(model,path_name)

def charge_modele(name):
    path_name = os.path.join(PATH,name)
    joblib.load(path_name)

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

linearReg = LinearRegression()
linearReg.fit(housing_prepared,housing_labels)
predictions = linearReg.predict(housing_prepared_test)

calcul_score(label_test,predictions)

tree = DecisionTreeRegressor()
tree.fit(housing_prepared,housing_labels)
predictions_tree = tree.predict(housing_prepared_test)

calcul_score(label_test,predictions_tree)

forest = RandomForestRegressor()
forest.fit(housing_prepared,housing_labels)

validation_score(linearReg)
validation_score(tree)
validation_score(forest)

sauvegarde_modele('LinearReg',linearReg)
sauvegarde_modele('Tree',tree)
sauvegarde_modele('Forest',forest)





