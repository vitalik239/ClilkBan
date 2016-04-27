# -*- coding: utf8 -*-

import pymorphy2

morph = pymorphy2.MorphAnalyzer()
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.decode('utf-8')


def get(word):
    good_candidates = _get_known_edits2(word)
    if not good_candidates:
        return '***'
    else:
        return good_candidates.pop()


def _is_good(word):
    return morph.word_is_known(word)


def _get_edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [spll + splr[1:] for spll, splr in splits if splr]
    transposes = [spll + splr[1] + splr[0] + splr[2:] for spll, splr in splits if len(splr) > 1]
    replaces = [spll + letter + splr[1:] for spll, splr in splits for letter in alphabet if splr]
    inserts = [spll + letter + splr for spll, splr in splits for letter in alphabet]
    return set(deletes + transposes + replaces + inserts)


def _get_known_edits2(word):
    edits1_set = _get_edits1(word)
    return set(edit2 for edit1 in edits1_set for edit2 in _get_edits1(edit1) if _is_good(edit2))

