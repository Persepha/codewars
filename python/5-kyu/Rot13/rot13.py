def rot13(message):
    result = ''
    for char in message:
        if 65 <= ord(char) <= 90:
            result += chr(65 + (ord(char) + 13 - 65) % 26)
        elif 97 <= ord(char) <= 122:
            result += chr(97 + (ord(char) + 13 - 97) % 26)
        else:
            result += char
    return result
