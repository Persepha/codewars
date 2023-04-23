function sortArray(array) {
    sortedOddNumbers = array.filter(x => x % 2 !== 0).sort((a, b) => b - a)
    return array.map(x =>  x % 2 === 0 ? x : sortedOddNumbers.pop())
}
