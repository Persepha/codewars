def sum_of_digits(number):
    return sum(int(digit) for digit in number)

def order_weight(strng):
    return " ".join(sorted(strng.split(), key=lambda x: (sum_of_digits(x), x)))
