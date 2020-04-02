def find_outlier(integers):
    even = odd = None
    even_count = odd_count = 0
    for i in integers:
        if i % 2 == 0:
            even = i
            even_count += 1
        else:
            odd = i
            odd_count += 1

    return even if even_count < odd_count else odd
