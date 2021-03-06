def averageAge(array):
    '''
    A function named averageAge which computes the average age of every person obect which is present in a list

    Parameter: array, array is a list of dictionary which contains two keys: name and age in each cases.

    Returns: The average age.
    
    @author: Babatunde Koiki
    Created on 2020-03-28
    '''
    return sum([j['age']for j in array])/len([j['age']for j in array])

