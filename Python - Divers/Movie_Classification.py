import io
import os
import string
import re

from os import listdir
from os.path import isfile, join,isdir

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import cross_val_score

# Déclaration des variables
liste_old = []
liste_new = []
liste_manquant = []

Path = 'E:\\OneDrive\Divers\\Listes\\3 - Liste Films\\2019\\Liste Movies Category'
separator ='\\'
Destination = 'Missing Movies.txt'

# Création d'un dictionnaire à partir d'un ensemble de fichiers
def generate_dictionnary(pathFile):
    listeMovies=[]
    listeCategories=[]
    onlyfiles = [f for f in listdir(pathFile) if isfile(join(pathFile, f))]

    for filenames in onlyfiles:
        fileName = separator.join((pathFile,filenames))           
        with io.open(fileName, mode="r",encoding="utf-16") as f:
                for index,line in enumerate(f):
                    if index > 2:
                        if line.strip('\n').rstrip() != '':
                            listeMovies.append(line.strip('\n').rstrip())
                            listeCategories.append(filenames)
    dictionnaire_films = {'Nom film':listeMovies,'Catégorie':listeCategories}
    return dictionnaire_films

pandas_films = pd.DataFrame(generate_dictionnary(Path))

def categorie_famille(title):
    if title[0:2]=='An':
        return 'Animation'
    if title[0:2]=='Av':
        return 'Average'
    if title[0:2]=='Bl':
        return 'Blockbusters'
    if title[0:2]=='Cl':
        return 'Classic'   
    if title[0:2]=='Do':
        return 'Documentary'
    if title[0:2]=='Fr':
        return 'Foreign'        
    if title[0:2]=='Go':
        return 'Good'  
    else:
        return 'Unknown'

def is_good(title):
    if title[:5]=='Good_' and title[5] != 'F':
        return True
    else:
        return False

def year_good(title):
    return title[5]+title[6]+title[7]+title[8]

def nationalite_film(title):
    if 'French' in title:
        return 'French'
    elif 'Foreign' in title:
        return 'Foreign'
    else:
        return 'US'

def date_release(title):
    occurence = re.findall('[0-9]{4}',title)
    list_year = list()

    for occ in occurence:
        if int(occ) > 1900 and int(occ) <2020:
            list_year.append(occ)

    try:
        release_year = min(list_year)
    except:
        release_year = 'NA'
    
    return release_year

def number_letter(title):
    return(len(title))

def extension(title):
    return title[-4:]

pandas_films['length_title'] = pandas_films['Nom film'].apply(number_letter)

pandas_films['extension'] = pandas_films['Nom film'].apply(extension)

pandas_films['Famille'] = pandas_films['Catégorie'].apply(categorie_famille)

pandas_films['Country'] = pandas_films['Catégorie'].apply(nationalite_film)

pandas_films['Release_Date'] = pandas_films['Nom film'].apply(date_release)

pandas_films['Is_Good'] = pandas_films['Catégorie'].apply(is_good)

print(pandas_films.columns)

proprietes_movies = pandas_films[['length_title', 'extension', 'Famille',
       'Country', 'Release_Date']]

target_movies = pandas_films['Is_Good']

##################################################################
# Encodages des features

labelencoder=LabelEncoder()

proprietes_movies_encode = {}

for col in proprietes_movies.columns:
    try:
        colEncode = labelencoder.fit_transform(proprietes_movies[col])
        label = col + '_encode'
        proprietes_movies_encode[label] = colEncode
    except:
        print(col)
        print(proprietes_movies[col].unique())

target_movies_encode = labelencoder.fit_transform(target_movies)

proprietes = pd.DataFrame(proprietes_movies_encode)

print(type(proprietes))
print(type(target_movies_encode))

scaler = StandardScaler().fit(proprietes)
proprietesNR = scaler.transform(proprietes)

Features_train, Features_test, Label_train, Label_test = train_test_split(proprietesNR, 
                                                                          target_movies_encode, 
                                                                          test_size=0.2)

##################################################################
# Création de le baseline KNN
parametres_knn = {'n_neighbors': np.arange(5, 10),
                  'metric':["euclidean",
                            "manhattan"],
                   'weights' : ['uniform',
                                'distance']}

baseLineKNN = GridSearchCV(
                        estimator=KNeighborsClassifier(),
                        param_grid=parametres_knn,
                        cv=5,
                        scoring='accuracy')   

baseLineKNN.fit(Features_train,
                Label_train)      

print('Les paramètres optimaux pour la base KNN sont les suivants : {}'.
      format(baseLineKNN.best_params_))

             
##################################################################
# Ensemble des modèles comparés
Modeles = {'KNN': baseLineKNN
           }

for title,model in Modeles.items():
    # Calcul des prédictions du modèle
    predictions = model.predict(Features_test)
    c_matr = confusion_matrix(Label_test, predictions)
    
    print(c_matr)

    print(' ' + '-' * 80)
    print('          Performance du modèle {0}'.format(title.upper()))
    print(' ' + '-' * 80)    
    
    # Tableau des erreurs :
    erreur=0
    # En tête du tableau
    print('\nDétail des erreurs :\n\n {0:37s}| {1:37s}| {2:s}'
          .format('Classe réelle (n°)', 
                  'Classe prédite (n°)',
                  'Qté'))
    print(' ' + '-' * 80)
    
    # Détail des erreurs
    for indice,row in enumerate(Label_test):
        if row != predictions[indice]:
            print('Valeur prédite : {} --- Valeur réelle : {} '.format(row,
                                                                       predictions[indice]))
    
    # Revue des performances
    score=(1-accuracy_score(Label_test, predictions))*len(Features_test)
    
    print(' ' + '-' * 80)
    
    print('Score de la prédiction {0} : {1:.2f}%'.
          format(title,
                  100*accuracy_score(Label_test, 
                                             predictions)))
    
    print('--- soit {0} prédictions correctes sur {1}).'.
         format(len(Label_test) - erreur, len(Label_test)))
    
    print('--- soit {0} erreurs de prédicition sur {1}).'.
         format(erreur, len(Label_test)))
    
    print(' ' + '-' * 80)
    print('')


