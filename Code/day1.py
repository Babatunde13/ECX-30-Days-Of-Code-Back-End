def litmus(x, y):
    '''
    A function named litmus which checks if it's parameters are positive or negative.

    Parameters: x and y, both integers

    Return: 
    '''
    try: 
        if x > 0 and y > 0: # Checks if both of them aregreater than 0.
            return f'{x} and {y} are both positive.'
        elif x > 0 and y < 0: # Checks is first is greater than 0 while the other is less t.han 0
            return f'{x} is positive and {y} is negative.'
        elif x < 0 and y> 0:  # Checks is first is less than 0 while the other is greater than 0.
            return f'{x} is negative and {y} is positive.'
        else:  # Checks if both of them aregreater than 0
            return f'{x} and {y} are both negative.'
    except: # If not a number
        return 'Something went wrong.'
