def more_zeros(s):
    characters = list(dict.fromkeys(s))
    return [x for x in characters if bin(ord(x))[2:].count('0') > bin(ord(x))[2:].count('1')]
