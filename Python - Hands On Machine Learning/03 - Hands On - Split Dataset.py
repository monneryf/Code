import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import hashlib

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

PATH = "E:\\Data\\Hands-on-Machine-Learning"
NAME_FILE = "housing.csv"

def importation_donnees(chemin,nom_fichier):
    file_name = os.path.join(chemin,nom_fichier)
    data = pd.read_csv(file_name)
    return data

def apercu_des_donnes():
    print(housing["ocean_proximity"].value_counts())
    print(housing.describe())

    housing.hist(bins=50,figsize=(20,15))
    plt.show()

def split_train_test(ratio,data_set):
    indices = np.random.permutation(len(data_set))
    indices_test = indices[int(len(data_set)*ratio):]
    indices_train = indices[:int(len(data_set)*ratio)]
    
    return data_set.iloc[indices_test],data_set.iloc[indices_train]

def test_check(identifier,ratio_test,hash):
    last_byte = hash(np.int64(identifier)).digest()[-1]
    plafond = int(ratio_test * 256)
    return last_byte < plafond

def split_train_test_hash(data_set,test_ratio,id_column,hash=hashlib.md5):
    ids=data_set[id_column]
    function_evaluation = lambda x : test_check(x,test_ratio,hash)
    in_test_set = ids.apply(function_evaluation)
    return data_set[~in_test_set],data_set[in_test_set]

def picking_data():
    #test,train = split_train_test(0.8,housing)
    housing_with_id = housing.reset_index()
    test,train = split_train_test_hash(housing_with_id,0.2,"index")
    print(test.shape)
    print(train.shape)

def categorie_income():
    housing["income_cat"] = np.ceil(housing['median_income']/1.5)
    housing["income_cat"].where(housing['income_cat']<5,5.0,inplace=True)

def split_simple():
    categorie_income()
    train,test = train_test_split(housing,
                                  test_size=0.2,
                                  random_state=42)
    #plt.hist(housing["income_cat"])
    #plt.show()
    print(train["income_cat"].value_counts())
    print(train["income_cat"].value_counts()/len(train["income_cat"]))

def split_stratifie():
    categorie_income()
    split= StratifiedShuffleSplit(n_splits=1,
                                  test_size=0.2,
                                  random_state=42)

    for train_index,test_index in split.split(housing,housing["income_cat"]):
        strat_train = housing.loc[train_index]
        strat_test = housing.loc[test_index]
    
    print(strat_train["income_cat"].value_counts())
    print(strat_train["income_cat"].value_counts()/len(strat_train["income_cat"]))

    return strat_train,strat_test

def first_step():    
    # split_simple()
    strat_train_set,strat_test_set = split_stratifie()
    
    for _set in (strat_train_set,strat_test_set):
        _set.drop("income_cat",axis=1,inplace=True)

    return strat_train_set,strat_test_set

housing = importation_donnees(PATH,NAME_FILE)
train, test = first_step()









