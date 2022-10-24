def is_valid(x):
    return 10 > x >= 0 and str(x).isdigit()


def up_array(arr):
    if not arr or not all(map(is_valid, arr)):
        return None

    number = int(''.join(map(str, arr))) + 1

    return list(map(int, str(number).zfill(len(arr))))
