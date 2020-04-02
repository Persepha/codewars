def snail(array):
    sorted_array = []

    while len(array) > 0:
        sorted_array.extend(array[0])
        del array[0]

        if len(array) > 0:
            for i in array:
                sorted_array.append(i[-1])
                del i[-1]
            
            sorted_array.extend(array[-1][::-1])
            del array[-1]

            for i in reversed(array):
                sorted_array.append(i[0])
                del i[0]

    return sorted_array
