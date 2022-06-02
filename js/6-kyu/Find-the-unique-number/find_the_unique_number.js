function findUniq(arr) {
    return arr.find(number => arr.indexOf(number) === arr.lastIndexOf(number))
}
