def cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1
    dividend = 1
    count = 0
    while True:
        dividend *= 10
        dividend %= n
        count += 1
        if dividend == 1:
            break
    return count