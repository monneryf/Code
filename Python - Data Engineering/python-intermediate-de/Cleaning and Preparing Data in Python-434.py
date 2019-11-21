## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)



## 2. Reading our MoMA Dataset ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

#close the opened file
opened_file.close()

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
with open('artworks.csv') as opened_file:
    read_file = reader(opened_file)
    moma = list(read_file)
    moma = moma[1:]


## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace('one','two')


## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

def cleaning(index):
    for row in moma:
        nationality = row[index]
        nationality = nationality.replace('(','')
        nationality = nationality.replace(')','')
        row[index] = nationality

cleaning(2)
cleaning(5)

    

## 5. String Capitalization ##

def cleaning(index,missing):
    for row in moma:        
        buffer = row[index]
        if buffer == '':
            buffer = missing
        else:
            buffer = buffer.replace('(','')
            buffer = buffer.replace(')','')
            buffer = buffer.title()
        row[index] = buffer
        
cleaning(2,'Nationality Unknown')
cleaning(5,'Gender Unknown/Other')


## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

def cleaning(index):
    for row in moma:
        row[index] = clean_and_convert(row[index])
    
cleaning(3)
cleaning(4)


## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(word):
    for char in bad_chars:
        word = word.replace(char,'')
    return word

stripped_test_data = list()

for stuff in test_data:
    stripped_test_data.append(strip_characters(stuff))
    
    

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(word):
    if '-' in word:
        bornes = word.split('-')
        return round((int(bornes[0])+int(bornes[1]))/2,0)
    else:
        return int(word)
    
processed_test_data = list()

for item in stripped_test_data:
    processed_test_data.append(process_date(item))
    
for row in moma:
    row[6] = process_date(strip_characters(row[6]))
    
    



## 9. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

print("{}'s birth year is {}".format(artist,birth_year))



## 10. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = " The population of {country} is {population:,.2f} million"

for land in pop_millions:
    print(template.format(country=land[0],population=land[1]))
    
    
    