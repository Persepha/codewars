def find_missing_number(numbers):
    missing_number = set(range(1, len(numbers)+2)) - set(numbers)
    return missing_number.pop()
