def adjacent_element_product(array):
    max_product = array[0] * array[1]
    array_len = len(array)
    for i in range(array_len-1):
        if array[i] * array[i+1] > max_product:
            max_product = array[i] * array[i+1]
    return max_product
