import datetime
def futurePast(date="22-02-2020"):
    '''
    A function named futurePast which checks if a date is passed.

    Parameter: takes the date which we want to compare with today as a string in the format dd-mm-yyyy

    Return: Passed if date has been passed, otherwse Not Passes
    
    @author: Babatunde Koiki
    Created on 2020-03-28
    '''
    present_date = datetime.datetime.now() # Presents date
    if present_date > datetime.datetime.strptime(date, '%d-%m-%Y'): # Compares present_date with the passed date.
        return "Passed."
    return "Not Passed"


print(futurePast())