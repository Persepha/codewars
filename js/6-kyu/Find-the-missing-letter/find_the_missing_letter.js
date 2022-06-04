function findMissingLetter(array) {
    return String.fromCharCode(array.find( (letter, index) => array[index+1].charCodeAt() - letter.charCodeAt() > 1).charCodeAt() + 1)
}
