## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for row in moma:
    date = row[6]
    if date != '':
        date = int(date)
    row[6] = date
    
    

## 2. Calculating Artist Ages ##

ages = list()

for row in moma:
    date = row[6]
    birth = row[3]
    
    if type(birth) == int:
        age = date-birth
    else:
        age = 0
        
    ages.append(age)        
        
final_ages = list()

for row in ages:
    if row>20:
        final_ages.append(row)
    else:
        final_ages.append('Unknown')
        
        

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen

decades = list()

for value in final_ages:
    if value=='Unknown':
        decade = value
    else:
        decade = str(value)
        decade = decade[:-1]
        decade = decade + "0s"
    
    decades.append(decade)

    

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

decade_frequency = dict()

for value in decades:
    if value in decade_frequency:
        decade_frequency[value]+=1
    else:
        decade_frequency[value]=1

        
        

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

template = "{name}'s birth year is {birth}"
output = template.format(name=artist,
                         birth=birth_year)

print(output)



## 6. Creating an Artist Frequency Table ##

artist_freq = dict()

for item in moma:
    artist = item[1]
    if artist not in artist_freq:
        artist_freq[artist]=1
    else:
        artist_freq[artist]+=1
        
print(artist_freq)



## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    template="There are {number} artworks by {name} in the data set"
    artworks = artist_freq[artist]
    output = template.format(number=artworks,
                             name=artist)
    
    print(output)
    
artist_summary("Henri Matisse")


                             

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for land in pop_millions:
    country = land[0]
    population = land[1]
    template = "The population of {0} is {1:,.2f} million"
    output = template.format(country,population)
    
    print(output)
    


## 9. Challenge: Summarizing Artwork Gender Data ##

freq_gender = dict()

for row in moma:
    gender = row[5]
    if gender in freq_gender:
        freq_gender[gender]+=1
    else:
        freq_gender[gender]=1

template = "There are {0:,} artworks by {1} artists"

for genre in freq_gender:
    output = template.format(freq_gender[genre],genre)
    print(output)
    
    