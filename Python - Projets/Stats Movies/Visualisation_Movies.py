import io
import os
import string
import re

from os import listdir
from os.path import isfile, join,isdir

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

#import locale
#locale.getdefaultlocale()

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

pandas_films['Famille'] = pandas_films['Catégorie'].apply(categorie_famille)

pandas_films['Country'] = pandas_films['Catégorie'].apply(nationalite_film)

pandas_films['Release_Date'] = pandas_films['Nom film'].apply(date_release)

pandas_films['Is_Good'] = pandas_films['Catégorie'].apply(is_good)

pandas_films_good = pandas_films[pandas_films['Is_Good']==True]

pandas_films_good['Year_Good'] = pandas_films_good['Catégorie'].apply(year_good)

func = lambda x: round(100*x.count()/pandas_films.shape[0],2)
agg_func={'Number': np.sum,
          'Ratio': func}

tcd_categorie = pandas_films.pivot_table(index='Catégorie',values='Nom film',aggfunc='count',margins=True)
tcd_categorie_ratio = pandas_films.pivot_table(index='Catégorie',values='Nom film',aggfunc=func,margins=True)

tcd_famille = pandas_films.pivot_table(index='Famille',values='Nom film',aggfunc='count')
tcd_famille_ratio = pandas_films.pivot_table(index='Famille',values='Nom film',aggfunc=func)

tcd_country = pandas_films.pivot_table(index='Country',values='Nom film',aggfunc='count')
tcd_country_ratio = pandas_films.pivot_table(index='Country',values='Nom film',aggfunc=func)

tcd_release = pandas_films.pivot_table(index='Release_Date',values='Nom film',aggfunc='count')
tcd_release_ratio = pandas_films.pivot_table(index='Release_Date',values='Nom film',aggfunc=func)

tcd_good_year = pandas_films_good.pivot_table(index='Year_Good',values='Nom film',aggfunc='count')
tcd_good_year_ratio = pandas_films_good.pivot_table(index='Year_Good',values='Nom film',aggfunc=func)

#print(pandas_films.head(5))
#print(pandas_films.tail(5))

print(tcd_categorie)

print(tcd_famille)

print(tcd_country)

print(tcd_release)

liste_df = [tcd_famille,
            tcd_famille_ratio,
            tcd_country,
            tcd_country_ratio,
            tcd_categorie,
            tcd_categorie_ratio,
            tcd_release,
            tcd_release_ratio,
            tcd_good_year,
            tcd_good_year_ratio]

for df in liste_df:
    df.to_csv(r'C:\\Users\\monne\\Desktop\\Stats_Movies.txt', header=True, index=True, sep=' ', mode='a')

saveFile = 'C:\\Users\\monne\\Desktop\\Stats_Movies_detail.txt'

print(type(tcd_categorie))
print(tcd_categorie)

with open(saveFile,'w') as outfile:
    for df in liste_df:
        outfile.writelines('---'*30)
        outfile.writelines('\n')
        df.to_string(outfile)
        outfile.writelines('\n')

#categorie = pd.Series(tcd_categorie.values,
#                      index=tcd_categorie.index)
#categorie.plot()

#print(type(list(tcd_categorie)))
#print(list(tcd_categorie))

#fig, ax = plt.subplots()
#ax.hist(tcd_categorie['Nom film'])
        #, range=(0, 5))

#tcd_famille.plot.barh()

tcd_famille.plot.pie(subplots=True)

tcd_good_year.plot.barh()

plt.show()












