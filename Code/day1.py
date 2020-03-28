def litmus(x, y):
    '''
    A function named litmus which checks if it's parameters are positive or negative.

    Parameters: x and y, both integers

    Return: 
    '''
    try:
        if x > 0 and y > 0:
            return f'{x} and {y} are both positive.'
        elif x > 0 and y < 0:
            return f'{x} is positive and {y} is negative.'
        elif x < 0 and y> 0:
            return f'{x} is negative and {y} is positive.'
        else:
            return f'{x} and {y} are both negative.'
    except:
        return 'Something went wrong.'
