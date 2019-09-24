## 1. Storing Data ##

content_ratings = ['4+','9+','12+','17+']
numbers = [4433,987,1155,622]

content_rating_numbers = [content_ratings,numbers]



## 2. Dictionaries ##

content_ratings = {'4+':4433,'9+':987,'12+':1155,'17+':622}
print(content_ratings)




## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

over_9 = content_ratings['9+']
over_17 = content_ratings['17+']

print(over_9)
print(over_17)




## 4. Alternative Way of Creating a Dictionary ##

content_ratings = {}

content_ratings['4+']=4433
content_ratings['9+']=987
content_ratings['12+']=1155
content_ratings['17+']=622

over_12_n_apps = content_ratings['12+']



## 5. Key-Value Pairs ##

d_1 = {}
error = True

d_1['key_1']= 'first_value'
d_1['key_2']=2
d_1['key_3']=3.14
d_1['key_4']= error
d_1['key_5']=[4,2,1]
d_1['key_6']= {'inner_key' : 6}



## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings:
    result='It exists'
    

    

## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+':0,'9+':0,'12+':0,'17+':0}

for row in apps_data[1:]:
    if row[10] in content_ratings:
        content_ratings[row[10]]+=1

print(content_ratings)


    

## 8. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}

for row in apps_data[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating]+=1
    else:
        content_ratings[c_rating]=1

print(content_ratings)




## 9. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}

for row in apps_data[1:]:
    genre=row[11]
    if genre in genre_counting:
        genre_counting[genre]+=1
    else:
        genre_counting[genre]=1
        
print(genre_counting)




## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for value in content_ratings:
    content_ratings[value] /= total_number_of_apps
    content_ratings[value] *= 100
    
percentage_17_plus = content_ratings['17+']

percentage_15_allowed = 100 - percentage_17_plus



## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for value in content_ratings:
    c_ratings_proportions[value] = content_ratings[value] / total_number_of_apps
    c_ratings_percentages[value] = c_ratings_proportions[value]*100
    
    
    
    


## 12. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = list()

for row in apps_data[1:]:
    data_sizes.append(int(row[2]))
    
min_size = min(data_sizes)
max_size = max(data_sizes)




## 13. Filtering for the Intervals ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_count_tot = list()
frequency = {}

for row in apps_data[1:]:
    rating_count_tot.append(int(row[5]))                            

mini = min(rating_count_tot)
maxi = max(rating_count_tot)

inter = int((max(rating_count_tot) - min(rating_count_tot))/20)+1                           

print(mini)
print(maxi)

for row in apps_data[1:]:
    for num in range(20):
        rating = int(row[5])
        plancher = mini + num*inter
        plafond = mini + (num+1)*inter
        
        libelle = str(plancher) + " - " + str(plafond)
        
        if (rating >plancher) and (rating <= plafond):
            if libelle in frequency:
                frequency[libelle]+=1
            else:
                frequency[libelle]=1
                                                  
print(frequency)    
    
    
    
    
    
    
                                