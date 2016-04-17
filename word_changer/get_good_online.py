import csv
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
baddict = {}


class Good:

    def __init__(self):
        with open('/Users/vitalik/Desktop/ClilkBan/resources/bad-good.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            for key, value in reader:
                baddict[key] = value

    def make_good(word):
        p = morph.parse(word)[0]
        norm = p.normal_form
        if morph in baddict:
            return baddict[word]
        elif norm in baddict:
            return baddict[norm]
        else:
            return word
