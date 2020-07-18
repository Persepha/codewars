VOWELS = 'aeiou'

def encode(st):
    return ''.join(str(VOWELS.index(letter) + 1) if letter in VOWELS else letter for letter in st)

def decode(st):
    return ''.join(VOWELS[int(letter)-1] if letter.isdigit() else letter for letter in st)
