def remove_duplicate_words(s):
    words = s.split(None)
    unique_words = list(dict.fromkeys(words))
    return ' '.join(unique_words)
