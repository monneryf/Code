## 1. Storing Data ##

content_ratings = ['4+', '9+', '12+', '17+']

number = [4433, 987, 1155, 622] 

content_rating_numbers = [content_ratings,number]


## 2. Dictionaries ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print(content_ratings)



## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

over_9 = content_ratings['9+']

over_17 = content_ratings['17+']

print(over_9)

print(over_17)



## 4. Alternative Way of Creating a Dictionary ##

content_ratings = {} 
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']

## 5. Key-Value Pairs ##

d_1 = {'key_1': 'first_value', 
 'key_2': 2,
 'key_3': 3.14,
 'key_4': True,
 'key_5': [4,2,1],
 'key_6': {'inner_key' : 6}
 }

error = True



## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings:
    result = "It exists"
    print(result)

# Alternative solution
is_in_dictionary = '17+' in content_ratings
if is_in_dictionary:
    result = "It exists"
    print(result)
    
    

## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

content_ratings = dict()

for data in apps_data[1:]:
    if data[10] in content_ratings:
        content_ratings[data[10]] +=1
    else:
        content_ratings[data[10]] =1
        
print(content_ratings)



## 8. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

content_ratings = dict()

for data in apps_data[1:]:
    if data[10] in content_ratings:
        content_ratings[data[10]] +=1
    else:
        content_ratings[data[10]] =1
        
print(content_ratings)




## 9. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader

read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

genre_counting = dict()

for genre in apps_data[1:]:
    if genre[11] in genre_counting:
        genre_counting[genre[11]] += 1
    else:
        genre_counting[genre[11]] = 1

print(genre_counting)


## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

percentage_17_plus = (content_ratings['17+'] / total_number_of_apps)*100

percentage_15_allowed = ((content_ratings['4+'] + content_ratings['9+'] + content_ratings['12+'] ) / total_number_of_apps)*100





## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = dict()
c_ratings_percentages = dict()

for rating in content_ratings:
    c_ratings_proportions[rating] = content_ratings[rating] / total_number_of_apps
    c_ratings_percentages[rating] = c_ratings_proportions[rating] * 100
    
    

## 12. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader

read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

data_sizes = list()

for size in apps_data[1:]:
    data_sizes.append(float(size[2]))
    
min_size = min(data_sizes)
max_size = max(data_sizes)
