## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]

mean = sum(distribution) / len(distribution)

mid = int(len(distribution) / 2)

center = (mean == mid)

under_sum = 0
upper_sum = 0

for value in distribution:
    if value <= mean:
        under_sum+= abs(mean-value)
    else:
        upper_sum+= abs(mean-value)
    
equal_distances = (under_sum == upper_sum)



## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed

equal_distances = 0

for value in range(5000):
    seed(value)
    vector = randint(1000,size=10)
    mean = vector.mean()
    upper_mean=0
    under_mean=0
    
    for nb in vector:
        if nb <= mean:
            under_mean+=mean-nb
        else:
            upper_mean+=nb-mean
            
    if round(under_mean,1) == round(upper_mean,1):
        equal_distances+=1

print(equal_distances)



## 4. Defining the Mean Algebraically ##

one = False
two = False
three = False



## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def moyenne(numbers):
    somme=0
    for value in numbers:
        somme+=value
    return somme / len(numbers)

mean_1 = moyenne(distribution_1)
mean_2 = moyenne(distribution_2)
mean_3 = moyenne(distribution_3)



## 6. Introducing the Data ##

houses = pd.read_table('AmesHousing_1.txt')

one = True
two = False
three = True



## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses['SalePrice'])

pandas_mean = houses['SalePrice'].mean()

means_are_equal = function_mean == pandas_mean



## 8. Estimating the Population Mean ##

parameter = houses['SalePrice'].mean()
sample_size = 5

sample_sizes = []
sampling_errors = []

for i in range(101):
    sample = houses['SalePrice'].sample(sample_size , random_state = i)
    statistic = sample.mean()
    sampling_error = parameter - statistic
    sampling_errors.append(sampling_error)
    sample_sizes.append(sample_size)
    sample_size += 29
    
import matplotlib.pyplot as plt
plt.scatter(sample_sizes, sampling_errors)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')

## 9. Estimates from Low-Sized Samples ##

parameter = houses['SalePrice'].mean()
sample_size = 5

sample_sizes = []
sampling_errors = []

for i in range(10000):
    sample = houses['SalePrice'].sample(100 , random_state = i)
    statistic = sample.mean()
    sampling_error = parameter - statistic
    sampling_errors.append(statistic)
    sample_sizes.append(sample_size)
    sample_size += 29
    
import matplotlib.pyplot as plt
plt.hist(sampling_errors)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0,500000)

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]

samples = [[3, 7], [3, 2],
           [7, 2], [7, 3],
           [2, 3], [2, 7]]
           
sample_means = list()
           
for sample in samples:
    sample_means.append(sum(sample)/len(sample))
    
population_mean = sum(population) / len(population)    
mean_sample = sum(sample_means) / len(sample_means)

unbiased = mean_sample == population_mean

print(unbiased)
