import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import hashlib

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import StandardScaler

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion

from pandas.plotting import scatter_matrix

PATH = "E:\\Data\\Hands-on-Machine-Learning"
NAME_FILE = "housing.csv"

def importation_donnees(chemin,nom_fichier):
    file_name = os.path.join(chemin,nom_fichier)
    data = pd.read_csv(file_name)
    return data

def categorie_income():
    housing["income_cat"] = np.ceil(housing['median_income']/1.5)
    housing["income_cat"].where(housing['income_cat']<5,5.0,inplace=True)

def split_stratifie():
    categorie_income()
    split= StratifiedShuffleSplit(n_splits=1,
                                  test_size=0.2,
                                  random_state=42)

    for train_index,test_index in split.split(housing,housing["income_cat"]):
        strat_train = housing.loc[train_index]
        strat_test = housing.loc[test_index]
    
    #print(strat_train["income_cat"].value_counts())
    #print(strat_train["income_cat"].value_counts()/len(strat_train["income_cat"]))

    return strat_train,strat_test

def first_step():    
    strat_train_set,strat_test_set = split_stratifie()
    
    for _set in (strat_train_set,strat_test_set):
        _set.drop("income_cat",axis=1,inplace=True)

    return strat_train_set,strat_test_set

def export():
    housing = train.drop("median_house_value",axis=1)
    labels= train["median_house_value"]
    sauvegarde = os.path.join(PATH,'housing_labels.csv')

    labels.to_csv(sauvegarde, 
                        header=False, 
                        index=False, 
                        sep=',')

    housing_test = test.drop("median_house_value",axis=1)

    labels_test = test["median_house_value"]
    sauvegarde_test = os.path.join(PATH,'housing_labels_test.csv')

    labels_test.to_csv(sauvegarde_test, 
                        header=False, 
                        index=False, 
                        sep=',')

def encodage():
    housing = train.drop("median_house_value",axis=1)
    labels= train["median_house_value"]

    housing_num = housing.drop("ocean_proximity",axis=1)

    imputer = SimpleImputer(strategy="median")
    imputer.fit(housing_num)

    X = imputer.transform(housing_num)
    housing_tr = pd.DataFrame(X,columns=housing_num.columns)

    encoder = LabelEncoder()
    housing_cat = housing["ocean_proximity"]
    housing_cat_encoded = encoder.fit_transform(housing_cat)

    encoder = OneHotEncoder()
    housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))

    encoder = LabelBinarizer()
    housing_cat_1hot = encoder.fit_transform(housing_cat)

    total_X = pd.concat([housing_tr,pd.DataFrame(housing_cat_1hot)])
    return total_X

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    
    def fit(self, X, y=None):
        return self  # nothing else to do
    
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values

###############################################################################
########### DATASET ###########################################################
###############################################################################

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6
housing = importation_donnees(PATH,NAME_FILE)

train, test = first_step()
export()

housing = train.drop("median_house_value",axis=1)
labels= train["median_house_value"]
housing_num = housing.drop("ocean_proximity",axis=1)

housing_test = test.drop("median_house_value",axis=1)
labels= test["median_house_value"]
housing_num_test = housing_test.drop("ocean_proximity",axis=1)


###############################################################################
########### PIPELINE ##########################################################
###############################################################################

num_attribs = list(housing_num.columns)
cat_attribs = ["ocean_proximity"]

num_pipeline = Pipeline([
        ('selector', DataFrameSelector(num_attribs)),
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])

cat_pipeline = Pipeline([
        ('label_binarizer', LabelBinarizer()),
    ])

full_pipeline = FeatureUnion(transformer_list=[
        ("num_pipeline", num_pipeline),
        ("cat_pipeline", cat_pipeline),
    ])

###############################################################################
########### TRAIN #############################################################
###############################################################################

numie = num_pipeline.fit_transform(housing)

encoder = LabelBinarizer()
housing_cat = encoder.fit_transform(housing["ocean_proximity"])

print(numie.shape)
print(housing_cat.shape)

housing_prepared = pd.concat([pd.DataFrame(numie),pd.DataFrame(housing_cat)],axis=1)

print(type(housing_prepared))
print(housing_prepared.shape)

sauvegarde = os.path.join(PATH,'housing_prepared.csv')

housing_prepared.to_csv(sauvegarde, 
                        header=False, 
                        index=False, 
                        sep=',')

###############################################################################
########### TEST #############################################################
###############################################################################

numie_test = num_pipeline.fit_transform(housing_test)

encoder = LabelBinarizer()
housing_cat_test = encoder.fit_transform(housing_test["ocean_proximity"])

print(numie_test.shape)
print(housing_cat_test.shape)

housing_prepared_test = pd.concat([pd.DataFrame(numie_test),pd.DataFrame(housing_cat_test)],axis=1)

print(type(housing_prepared_test))
print(housing_prepared_test.shape)

sauvegarde_test = os.path.join(PATH,'housing_prepared_test.csv')

housing_prepared_test.to_csv(sauvegarde_test, 
                            header=False, 
                            index=False, 
                            sep=',')



