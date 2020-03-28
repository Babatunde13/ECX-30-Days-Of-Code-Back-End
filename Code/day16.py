def stringConverter(x):
    '''
    A function named stringConverter which casts a string to an integer and returns error if not possible.

    Parameter: A numeric string

    Return: The number as type int or error if not possible.
    '''

    try:
        return int(x)    

    except ValueError:
        return "Error"

