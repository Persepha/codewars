def is_pangram(s):
    return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
