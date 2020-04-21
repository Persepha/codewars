def rgb_to_hex(number):
    if number < 0:
        return '00'
    if number > 255:
        return 'FF'
    return format(number, '02X')

def rgb(r, g, b):
    return rgb_to_hex(r) + rgb_to_hex(g) + rgb_to_hex(b)
