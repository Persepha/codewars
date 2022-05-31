function duplicateCount(text){
    duplicateNumber = 0
    for (letter of new Set(text.toLowerCase()))
        if ((text.match(new RegExp(letter, 'ig')) || []).length > 1)
        duplicateNumber += 1
    return duplicateNumber
}