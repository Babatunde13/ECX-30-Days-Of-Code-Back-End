import datetime
from dateutil.relativedelta import relativedelta

def reminderFunction(date_of_birth="13-06-2002"):
    '''
    A function named reminderFunction which checks the number of days to the next birthday of a person.

    Parameter: takes the date which we want to compare with the birthday as a string in the format dd-mm-yyyy

    Return: Passed if date has been passed, otherwse Not Passes
    
    @author: Babatunde Koiki
    Created on 2020-03-28
    '''
    
    date_of_birth = datetime.datetime.strptime(date_of_birth, '%d-%m-%Y')
    present_date = datetime.datetime.now() # Present date
    val = present_date.year - date_of_birth.year # Computes the year difference
    if date_of_birth.month > present_date.month: # Checks if birthday has been done in the present year.
        date_of_birth = date_of_birth + relativedelta(years=present_date.year-date_of_birth.year)
        diff = present_date - date_of_birth 
    else:
        date_of_birth = date_of_birth + relativedelta(years=val)
        diff = date_of_birth - present_date 
    return abs(diff.days + 1)


print(reminderFunction())