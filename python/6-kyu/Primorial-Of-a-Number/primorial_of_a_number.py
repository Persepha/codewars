from functools import reduce

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            yield number
            count += 1
        number += 1

def num_primorial(n):
    return reduce((lambda x, y: x * y), get_primes(n))
