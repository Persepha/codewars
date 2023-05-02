def get_digit_from_word(word):
    return int("".join(character for character in word if character.isdigit()))


def order(sentence):
    return " ".join(sorted(sentence.split(), key=get_digit_from_word))
