function alphabetPosition(text) {
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return text.toLowerCase()
        .split('')
        .map(x => alphabet.indexOf(x) + 1)
        .filter(x => x)
        .join(' ')
}
