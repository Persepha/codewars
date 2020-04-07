def digital_root(n):
    while n > 9:
        n = sum(map(int, list(str(n))))

    return n
