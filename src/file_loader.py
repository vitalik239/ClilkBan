badwords = []


def get():
    file = open('resources/badwords.txt', 'rU')

    for word in file:
        word = word.strip(" \n")
        badwords.append(word.decode('utf-8'))