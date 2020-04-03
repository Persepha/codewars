def high(x):
    words = x.split()
    words_scores = [sum(ord(letter)-96 for letter in word) for word in words] 
    return words[words_scores.index(max(words_scores))]
