from math import sqrt


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def is_backward_prime(number):
    if str(number) == str(number)[::-1]:
        return False
    if is_prime(number) and is_prime(int(str(number)[::-1])):
        return True

    return False

def backwards_prime(start, stop):
    return [x for x in range(start, stop + 1) if is_backward_prime(x)]
