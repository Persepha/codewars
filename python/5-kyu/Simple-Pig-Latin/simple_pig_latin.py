def swapper(word):
    if len(word) > 1:
        word = word[1:] + word[0]
    word += 'ay'
    return word

def pig_it(text):
    return ' '.join(swapper(word) if word.isalpha() else word for word in text.split())
