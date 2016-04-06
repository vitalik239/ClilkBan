# -*- coding: utf8 -*-

import pymorphy2
import file_loader

morph = pymorphy2.MorphAnalyzer()

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.decode('utf-8')


def is_good(word):
    #p = morph.parse(word)[0]
    return morph.word_is_known(word) and word not in file_loader.badwords


def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if is_good(e2))


def known(words):
    return set(w for w in words if is_good(w))


def good(word):
    candidates1 = known([word]).union(known(edits1(word)))

    # candidates2 = candidates1.union(known_edits2(word))

    if not candidates1:
        suitable = '***'
    else:
        suitable = candidates1.pop()
    return suitable
