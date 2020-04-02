import re

def solve(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    highest_value = 0
    consonant_substrings = list(filter(None, re.split(r'[aeiou]', s)))
    
    for i in consonant_substrings:
        value = 0
        for consonant in i:
            value += alphabet.index(consonant) + 1
        if value > highest_value:
            highest_value = value
            
    return highest_value
