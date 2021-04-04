def parts_sums(ls):
    result = [0]
    for i in range(len(ls)):
        result.append(result[i]+ls.pop())
    return result[::-1]
