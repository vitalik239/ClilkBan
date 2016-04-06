import csv
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

class Good:
    dict = {}

    def __init__(self):
        reader = csv.reader(open('/Users/vitalik/Desktop/ClilkBan/resources/bad-good.csv', 'r'))
        for row in reader:
            key, value = row
            dict[key] = value
        print dict

    def make_good(self, word):
        p = morph.parse(word)
        norm = p.normal_form
        if word in dict:
            return dict[word]
        elif norm in dict:
            return dict[norm]
        else:
            return word
