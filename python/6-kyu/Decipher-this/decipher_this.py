import re

def decrypt_word(word):
    word = re.sub(r'(\d+)', lambda m: chr(int(m.group(0))), word)
    word = list(word)

    if len(word) > 2:
        word[1], word[-1] = word[-1], word[1]

    return ''.join(word)

def decipher_this(string):
    return ' '.join(decrypt_word(word) for word in string.split())
