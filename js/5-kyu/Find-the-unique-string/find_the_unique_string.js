function findUniq(arr) {
    formattedArray = arr.map(str => [...new Set(str.toLowerCase())].sort().join(''))
    return arr[formattedArray.findIndex(str => formattedArray.indexOf(str) === formattedArray.lastIndexOf(str))]
}
