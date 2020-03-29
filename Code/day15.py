def sentenceBuilder(data):
    '''
    A function named sentenceBuilder which forms a sentence from a the value in a list of dict

    Parameter: an array which contains dictionaries, these dictionaries contains only one key: value pair

    Returns: each of the values in a sentence form.
    
    @author: Babatunde Koiki
    Created on 2020-03-28
    '''

    list_ = [name['name'] for name in data] # Gets each value pair
    last = list_.pop() # Save the last element in the list and removs it from the list.
    return ', '.join(list_) + ' and ' + last # Turns the list to a string and do some stufss then return it.

