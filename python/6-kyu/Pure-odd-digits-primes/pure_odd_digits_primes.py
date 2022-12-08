def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_odd(n):
    return n % 2 != 0


def is_pure_odd_digits_prime(n):
    return is_prime(n) and all(is_odd(int(digit)) for digit in list(str(n)))


def get_next_odd_digits_prime(n):
    number = n + 1

    while (True):
        if is_pure_odd_digits_prime(number):
            return number
        number += 1


def only_oddDigPrimes(n):
    odd_digits_primes = [
        n
        for n in range(1, n + 1)
        if is_pure_odd_digits_prime(n)
    ]

    return [len(odd_digits_primes), odd_digits_primes[-1], get_next_odd_digits_prime(n)]
