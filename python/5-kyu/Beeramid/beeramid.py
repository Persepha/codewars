def beeramid(bonus, price):
    number_cans = bonus / price
    number_levels = 0
    while number_cans >= (number_levels + 1) ** 2:
        number_cans -= (number_levels + 1) ** 2
        number_levels += 1
    return number_levels
