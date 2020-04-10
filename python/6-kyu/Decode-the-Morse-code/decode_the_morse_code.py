def decodeMorse(morse_code):
    return ' '.join(''.join(MORSE_CODE[character] for character in word.split()) for word in morse_code.strip().split('   '))
