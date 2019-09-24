## 1. Introduction ##

from csv import reader

open_file = open('potus_visitors_2015.csv')
parser = reader(open_file)
potus = list(parser)

potus = potus[1:]




## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt

ibm_founded = dt.datetime(1911,6,16)

man_on_moon = dt.datetime(1969,7,20,20,17,0)



## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it



for row in potus:
    appt_start_date = row[2]
    appt_start_date_dt = dt.datetime.strptime(appt_start_date,"%m/%d/%y %H:%M")
    row[2] = appt_start_date_dt
    
    

## 6. Using Strftime to format dates ##

visitors_per_month = dict()

for row in potus:
    dt_object = row[2]
    key = dt_object.strftime("%B, %Y")
    if key not in visitors_per_month:
        visitors_per_month[key]=1
    else:
        visitors_per_month[key]+=1
        
print(visitors_per_month)


## 7. The Time Class ##

appt_times = list()

for row in potus:
    dt_object = row[2]
    dt_time = dt_object.time()
    appt_times.append(dt_time)
    
    



## 8. Comparing time objects ##

min_time = min(appt_times)
max_time = max(appt_times)

## 9. Calculations with Dates and Times ##

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days=56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)



## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    
appt_lengths = dict()

for row in potus:
    appt_start_date = row[2]
    appt_end_date = row[3]
    length = appt_end_date - appt_start_date
    if length in appt_lengths:
        appt_lengths[length]+=1
    else:
        appt_lengths[length]=1
        
min_length = min(appt_lengths)
max_length = max(appt_lengths)

