## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

wnba.head(5)
wnba.tail(5)

parameter = wnba['Games Played'].max()

sample = wnba['Games Played'].sample(random_state=1)

statistic = sample.max()

sampling_error = parameter-statistic



## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

statistic = list()

parameter = wnba['PTS'].mean()

for num_sample in range(100):
    sample = wnba['PTS'].sample(10,random_state=num_sample)
    statistic.append(sample.mean())
    
plt.scatter(range(1,101),statistic)

plt.axhline(parameter)



## 8. Proportional Stratified Sampling ##

print(wnba['Games Played'].value_counts(bins=3,normalize=True)*100)

inter = [0,12,22,100]
effectif = [1,2,7]

results = list()

for number in range(100):
    ensemble = list()
    for strat in range(3):        
        condition = (wnba.loc[:,'Games Played']>inter[strat]) & (wnba.loc[:,'Games Played']<=inter[strat+1])
        stratum = wnba.loc[condition,'PTS']
        ensemble.append(stratum.sample(effectif[strat],random_state=number))
    echantillon = pd.concat(ensemble)
    results.append(echantillon.mean())
    
plt.scatter(range(1,101),results)    
plt.axhline(wnba['PTS'].mean())

plt.show()
    

## 9. Choosing the Right Strata ##

wnba['MIN'].value_counts(bins = 3, normalize = True)



## 10. Cluster Sampling ##

clust = pd.Series(wnba['Team'].unique()).sample(4,random_state=0)
clusters = clust.tolist()
print(clusters)
conditions = (wnba['Team']==clusters[0]) | (wnba['Team']==clusters[1]) | (wnba['Team']==clusters[2]) | (wnba['Team']==clusters[3]) 

df = wnba.loc[conditions,:]

sampling_error_BMI = wnba['BMI'].mean() - df['BMI'].mean()
sampling_error_age = wnba['Age'].mean() - df['Age'].mean()
sampling_error_height = wnba['Height'].mean() - df['Height'].mean()
sampling_error_points = wnba['PTS'].mean() - df['PTS'].mean()



