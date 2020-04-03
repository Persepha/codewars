def letter_frequency(text):
    text = text.lower()
    data = [(letter, text.count(letter)) for letter in set(text) if letter.isalpha()]
    return sorted(data, key=lambda tup: (-tup[1], tup[0]))
