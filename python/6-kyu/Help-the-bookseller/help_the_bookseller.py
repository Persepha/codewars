def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ''
    books = []
    for category in listOfCat:
        books.append(f'({category} : {sum(int(x.split()[1]) for x in listOfArt if x.startswith(category))})')
    return ' - '.join(books)
