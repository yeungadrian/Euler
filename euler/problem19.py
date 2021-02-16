'''
Question
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

from datetime import datetime

def calculate_num_sundays(start_date='1900-01-01', end_date='2000-12-31'):

    '''
    Calculate the number of times sunday is the first day of the month between two dates

    Day 1: 1 Jan 1900

    List of the first days of the month
    1 + depending on the length of the month

    list_of_first_days = [1, 32, 50,...]

    Pythonically generate the list

    Days on sunday are divisible by 7 and need to subset any in 1900
    '''

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    list_of_firsts = [1]

    k = 1
    for j in range(0,101): # loop for the 100 years

        for i in range(1,13): # Loop for 12 months

            if i == 2:
                if j%4 == 0 & j!=0:  # february
                    k += 29
                else:
                    k += 28
                 
            elif i in [9,4,6,11]:
                k += 30
    
            else:
                k += 31
            
            list_of_firsts.append(k)   

        

    list_sundays =  [x for x in list_of_firsts if (x % 7 ==0 and x>365)]
    

    return(len(list_sundays))


print(calculate_num_sundays())