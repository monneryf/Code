import pyodbc

import io
import os
import string
import re

from os import listdir
from os.path import isfile, join,isdir

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

liste_old = []
liste_new = []
liste_manquant = []

Path = 'E:\\OneDrive\Divers\\Listes\\3 - Liste Films\\2019\\Liste Movies Category'
separator ='\\'
Destination = 'C:\\Users\\monne\\Desktop\\Failures.txt'

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
    elif title[0:2]=='Av':
        return 'Average'
    elif title[0:2]=='Bl':
        return 'Blockbusters'
    elif title[0:2]=='Cl':
        return 'Classic'   
    elif title[0:2]=='Do':
        return 'Documentary'
    elif title[0:2]=='Fr':
        return 'Foreign'        
    elif title[0:2]=='Go':
        return 'Good'
    else:
        return ''

def is_good(title):
    if title[:5]=='Good_' and title[5] != 'F':
        return True
    else:
        return False

def year_good(title):
    if title[0]=='G':
        return title[5]+title[6]+title[7]+title[8]
    else:
        return ''

def nationalite_film(title):
    if 'French' in title:
        return 'French'
    elif 'Foreign' in title:
        return 'Foreign'
    else:
        return 'US'

def date_release(title):
    release_year = ''
    occurence = re.findall('[0-9]{4}',title)
    list_year = list()

    for occ in occurence:
        if int(occ) > 1900 and int(occ) <2020:
            list_year.append(occ)

    try:
        release_year = min(list_year)
    except:
        release_year = ''
    
    return release_year

pandas_films['Famille'] = pandas_films['Catégorie'].apply(categorie_famille)
pandas_films['Country'] = pandas_films['Catégorie'].apply(nationalite_film)
pandas_films['Release_Date'] = pandas_films['Nom film'].apply(date_release)
pandas_films['Is_Good'] = pandas_films['Catégorie'].apply(is_good)
pandas_films['Year_Good'] = pandas_films['Catégorie'].apply(year_good)
#pandas_films['Year_Good'] = pandas_films['Year_Good'].fillna('',inplace=True)

print(pandas_films.shape)

def generate_request(Title,Category,DateRelease,Family,Country,Is_Good,Year_Good):
    if Is_Good ==True:
        Goodie=1
    else:
        Goodie=0

    if Year_Good ==None or Year_Good=='' or Year_Good=='Fren':
        Year_Good='NULL'
    
    if DateRelease=='':
        DateRelease = 'NULL'

    request = 'VALUES ("'
    request+= Title
    request+= '","'
    request+=Category
    request+='",'
    request+=DateRelease
    request+=',"'
    request+=Family
    request+='","'
    request+=Country
    request+='",'
    request+=str(Goodie)
    request+=','
    request+=str(Year_Good)
    request+=')'

    return request

server = 'DESKTOP-0SJ80TE\SQLEXPRESS'
database = 'Test'
table = 'Movies'

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-0SJ80TE\SQLEXPRESS;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('SET QUOTED_IDENTIFIER OFF')
cursor.commit()

with open(Destination,'a',encoding="utf-16") as outfile:
    #pandas_films.to_string(outfile)
    for index,row in pandas_films.iterrows():    
        request =generate_request(row['Nom film'],
                                 row['Catégorie'],
                                 row['Release_Date'],
                                 row['Famille'],
                                 row['Country'],
                                 row['Is_Good'],
                                 row['Year_Good'])

        request_db = 'INSERT INTO dbo.Movies (Title,Category,DateRelease,Family,Country,Is_Good,Year_Good) '
        request_db+= request
    
        try:
            cursor.execute(request_db)

        except:
            print(request_db)
            outfile.writelines('-'*30)
            outfile.writelines('\n')
            outfile.writelines(request_db)
            outfile.writelines('\n')

cursor.commit()

request = 'SELECT COUNT(*) FROM dbo.Movies;'
cursor.execute(request)

for row in cursor:
    print(row)
    


