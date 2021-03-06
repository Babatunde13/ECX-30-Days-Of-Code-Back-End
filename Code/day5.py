def noReverse(string):
    '''
    A function named noReverse which checks if a text is palindrome.

    Parameter: string, a text of type(str)

    Returns: Returns true if the string s palindrome.
    
    @author: Babatunde Koiki
    Created on 2020-03-28
    '''

    string = string.replace(' ', '') # Removes all the empty spaces
    if string.lower() == string[::-1].lower(): # Compares the string with it's reverse.
        return True
    return False
