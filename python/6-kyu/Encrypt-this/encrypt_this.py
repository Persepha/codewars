def encrypt_word(word):
    encrypted_word = ''
    if  word:
        encrypted_word += str(ord(word[0]))
    if len(word) == 2:
        encrypted_word += word[1:]
    if len(word) >= 3:
        encrypted_word += word[-1] + word[2:-1] + word[1]
    return encrypted_word

def encrypt_this(text):
    return ' '.join(encrypt_word(word) for word in text.split())
