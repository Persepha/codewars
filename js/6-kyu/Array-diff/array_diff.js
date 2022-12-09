function arrayDiff(a, b) {
    return a.filter(number => !b.includes(number))
}
