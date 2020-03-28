def vowel_counter(text):
    '''
    A function named vowel_counter which counts the number of vowels in the text.
    '''

    vowels = 'aeiou' # vowels variable
    return sum([text.lower().count(vowel) for vowel in vowels]) # Counts the number of time each vowel is present in text and sums it.

