def get_primes(n):
    a = list(range(n+1))
    a[1] = 0

    for i in a:
        if i:
            yield i
            for j in range(i**2, n+1, i):
                a[j] = 0

def decomp(n):
    primes = get_primes(n)
    decomposition = []
    for x in primes:
        count = 0
        number = n
        while number:
            number //= x
            count += number
        decomposition.append(f'{x}^{count}' if count > 1 else str(x))
    return ' * '.join(decomposition)
