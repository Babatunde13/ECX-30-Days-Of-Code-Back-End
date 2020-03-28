import datetime

def code_watch():
    '''
    A function named date

Parameters: None, the function doesn't take in any function.

    Returns: the day, hour, minute and second in a specified format.
    '''
    day, time = datetime.datetime.now().strftime('%A'), datetime.datetime.now().strftime('%I %p: %M : %S') 
    return f'Today is : {day}.\nCurrent time is : {time}'

