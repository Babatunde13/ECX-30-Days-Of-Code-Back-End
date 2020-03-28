import datetime

def date():
    day, time = datetime.datetime.now().strftime('%A'), datetime.datetime.now().strftime('%I %p: %M : %S') 
    return f'Today is : {day}.\nCurrent time is : {time}'

print(date())