def capitalize(s):
    result = []
    result.append(''.join([x.upper() if i % 2 == 0 else x for i, x in enumerate(s)]))
    result.append(''.join([x.upper() if i % 2 != 0 else x for i, x in enumerate(s)]))
    return result
