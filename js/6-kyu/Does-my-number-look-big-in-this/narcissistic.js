function narcissistic(value) {
    return value === value.toString().split('').reduce((sum, current, i, arr) => sum += current**arr.length, 0)
}
