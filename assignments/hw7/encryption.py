def encode(message, key):
    output = ''
    for letter in message:
        output += chr(ord(letter) + int(key))
    return output

def encode_better(message, word):
    messagel = []
    wordl = []
    wordl2 = []
    ad_message = []
    en_message = ''
    for letter in word:
        wordl += letter
    print(wordl)
    for i in range(len(message)):
        i = i % len(word)
        wordl2.append((ord(wordl[i])) - 65)
    print(wordl2)
    for letter in message:
        messagel.append(ord(letter) - 65)
    print(messagel)
    for i in messagel:
        for j in wordl2:
            ad_message.append(((i + j) % 58) + 65)
    print(ad_message)
    short_ad_message = ad_message[0:len(ad_message):len(message) + 1]
    for num in short_ad_message:
        en_message += chr(num)
    return en_message