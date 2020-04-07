def hamming_weight(x):
    count = 0
    while x:
        count += 1
        x &= x - 1

    return count
