const validWord = function(dictionary, word) {
    const allSubstring = dictionary.join('|')
    return new RegExp(`^(?:${allSubstring})+$`).test(word)
};
