def vowel_counter(text):
    '''
    A function named vowel_counter which counts the number of vowels in the text.
    '''
    vowels, count = 'aeiou', 0
    return sum([text.lower().count(vowel) for vowel in vowels])

