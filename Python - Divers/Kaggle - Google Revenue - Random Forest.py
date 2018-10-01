import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFECV
from sklearn.model_selection import GridSearchCV

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999

def dataset(Path,Name):

    pathFile = '\\'.join([Path,Name])

    dict_cols = ['trafficSource','totals','geoNetwork','device'] 

    df = pd.read_csv(pathFile, dtype={'fullVisitorId': 'str'}, nrows=None)

    for column in dict_cols:
        df = df.join(pd.DataFrame(df.pop(column).apply(pd.io.json.loads).values.tolist(), index=df.index))

    try:
        df['Revenue']=df['transactionRevenue']
    except:    
        df['Revenue']=0

    cols = df.columns.tolist()

    print('--'*30)
    print(df.shape)

    liste_features = ['Revenue',
                        'fullVisitorId', 
                        'source', 
                        'bounces', 
                        'hits', 
                        'newVisits', 
                        'pageviews', 
                        'visits', 
                        'subContinent', 
                        'browser', 
                        'deviceCategory', 
                        'isMobile', 
                        'operatingSystem']

    new_df = df[liste_features]

    col_dummies = [     'source',                     
                        'subContinent', 
                        'browser', 
                        'deviceCategory', 
                        'isMobile', 
                        'operatingSystem']

    for col in col_dummies:
        dummies = pd.get_dummies(new_df[col],prefix=col)
        new_df = pd.concat([new_df,dummies],axis=1)
        #new_df.drop(col)


    new_df = new_df.drop(col_dummies,axis=1)

    return new_df

Path = 'c:\\users\\monne\\Desktop\\Google Analytics Customers'
Name = 'train.csv'

train_features = dataset(Path,Name)
train_target = train_features.pop('Revenue')
train_id = train_features.pop('fullVisitorId')

Name = 'test.csv'

test_features = dataset(Path,Name)
test_target = test_features.pop('Revenue')
test_id = test_features.pop('fullVisitorId')

lr = LinearRegression()

lr.fit(train_features,train_target)
predictions_revenue = lr.predict(test_features)

mse = np.array((test_target - predictions_revenue)**2).sum()
rmse = np.sqrt(mse)

print('--'*20)
print(f'Mean square error : '.mse)
print(f'Root mean square error : '.rmse)
print('--'*20)

sub_df = pd.DataFrame({"fullVisitorId":test_id})
predictions_revenue[predictions_revenue < 0] = 0

sub_df["PredictedLogRevenue"] = np.expm1(predictions_revenue)
sub_df = sub_df.groupby("fullVisitorId")["PredictedLogRevenue"].sum().reset_index()
sub_df.columns = ["fullVisitorId", "PredictedLogRevenue"]

sub_df["PredictedLogRevenue"] = np.log1p(sub_df["PredictedLogRevenue"])

print('--'*20)
print(sub_df.head())
print('--'*20)

Path = 'c:\\users\\monne\\Desktop\\Google Analytics Customers'
Name = 'baseline_lgb.csv'
pathFile = '\\'.join([Path,Name])
sub_df.to_csv(pathFile, index=False)





