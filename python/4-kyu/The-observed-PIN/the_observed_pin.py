from itertools import product


def get_pins(observed):
    adjacent_digits = {
        '0': '08',
        '1': '124',
        '2': '2135',
        '3': '326',
        '4': '4157',
        '5': '52468',
        '6': '6359',
        '7': '748',
        '8': '85790',
        '9': '968'
    }

    digits = [adjacent_digits[x] for x in observed]
    pins = [''.join(pin) for pin in product(*digits)]
    return pins
