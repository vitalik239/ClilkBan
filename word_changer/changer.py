import get_good
import csv

badwords = []
words = {}


def get_badwords():
    bad_file = open('/Users/vitalik/Desktop/ClilkBan/resources/badwords.txt', 'rU')

    for badword in bad_file:
        badword = badword.strip(" \n")
        badwords.append(badword.decode('utf-8'))


def save_to_csv(dict):
    writer = csv.writer(open('/Users/vitalik/Desktop/ClilkBan/resources/bad-good.csv', 'wb'))
    for key, value in dict.items():
        writer.writerow([key.encode('utf-8'), value.encode('utf-8')])


get_badwords()
for word in badwords:
    words[word] = get_good.good(word)
save_to_csv(words)
