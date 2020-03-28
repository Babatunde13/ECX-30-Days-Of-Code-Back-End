def secret_map(*ele):
    '''
    A function named secret_map that squares every element passed into iy.
     Uses lambda and map.
    Parameter: Takes an infinite number of parameter and turns it into a list.

    Returns: The square of each element passed in as a list. 
    '''
    mapper = lambda a: a ** 2
    return list(map(mapper, ele))
    
print(secret_map(3, 4, 5))