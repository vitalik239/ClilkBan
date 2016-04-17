# -*- coding: utf8 -*-

import pymorphy2
#import changer

morph = pymorphy2.MorphAnalyzer()

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.decode('utf-8')


def is_good(word):
    p = morph.parse(word)[0]
    return morph.word_is_known(word)


def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits2(word):
    set_of_words = edits1(word)
    c = set(ww for w in set_of_words for ww in edits1(w) if is_good(ww))
    return c


def good(word):
    candidates = known_edits2(word)
    pp = morph.parse(word)[0]
    for c in candidates:
        p = morph.parse(c)[0]
        if p.tag.POS == pp.tag.POS and p.tag.case == pp.tag.case:
            return c
    return '***'
