# -*- coding: utf8 -*-

import csv
import pymorphy2
import argparse
import os.path

morph = pymorphy2.MorphAnalyzer()
bad_word_substs = {}


def load_dict(path):
    with open(path, 'r') as infile:
        reader = csv.reader(infile, delimiter=',')
        for key, value in reader:
            bad_word_substs[key.decode('utf-8')] = value


def make_good(word):
    p = morph.parse(word)[0]
    norm = p.normal_form
    if word in bad_word_substs:
        return bad_word_substs[word]
    elif norm in bad_word_substs:
        return bad_word_substs[norm]
    else:
        return word

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make some words good.')
    parser.add_argument('dict_path', type=str, help='path to dict')
    parser.add_argument('--words', nargs='*', help='word for proceeding')
    args = parser.parse_args()

    if not os.path.isfile(args.dict_path):
        print 'Wrong path to dictionary'
        exit()

    load_dict(args.dict_path)

    for word in args.words:
        print make_good(word.decode('utf-8'))
