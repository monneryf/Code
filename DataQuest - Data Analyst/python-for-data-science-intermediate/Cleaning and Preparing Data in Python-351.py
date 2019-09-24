## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)


## 2. Reading our MoMA Data Set ##

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

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
opened_file = open('artworks.csv')
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

def clean_row(row):
    clean = row.replace('(','')
    clean = clean.replace(')','')
    return clean

for row in moma:
    row[2] = clean_row(row[2])
    row[5] = clean_row(row[5])
    
    
    

## 5. String Capitalization ##

def capital(label,row):
    if row=='':
        capital_row = label + ' Unknown/Other'
    else:
        capital_row = row.title()
    
    return capital_row

def capital_n(label,row):
    if row=='':
        capital_row = label + ' Unknown'
    else:
        capital_row = row.title()
    
    return capital_row

for row in moma:
    row[2]=capital_n('Nationality',row[2])
    row[5]=capital('Gender',row[5])
    
    

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

for row in moma:
    row[3] = clean_and_convert(row[3])
    row[4] = clean_and_convert(row[4])
    
    

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
    stuff = strip_characters(stuff)
    stripped_test_data.append(stuff)
    

    

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
        new_number=0
        for number in word.split('-'):
            new_number+=int(number)
        return round(new_number/2)
    else:
        return int(word)
 
processed_test_data = list()

for stuff in stripped_test_data:
    processed_test_data.append(process_date(stuff))
    
print(processed_test_data)

for row in moma:
    clean_data = strip_characters(row[6])
    clean_date= process_date(clean_data)
    row[6] = clean_date
    
    
    
    
    