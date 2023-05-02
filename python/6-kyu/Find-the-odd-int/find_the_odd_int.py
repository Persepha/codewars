def find_it(seq):
    return [number for number in seq if seq.count(number) % 2 != 0][0]
