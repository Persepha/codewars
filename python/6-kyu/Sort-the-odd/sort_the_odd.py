def sort_array(source_array):
    sorted_odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)

    return [x if x % 2 == 0 else sorted_odds.pop() for x in source_array]
