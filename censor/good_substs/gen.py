import csv
import argparse
import word_subst
import os.path

bad_words = []
bad_word_substs = {}


def read_bad_words(bad_words_path):
    bad_file = open(bad_words_path, 'rU')
    for bad_word in bad_file:
        bad_word = bad_word.strip(" \n")
        bad_words.append(bad_word.decode('utf-8'))


def make_good_substs():
    for word in bad_words:
        bad_word_substs[word] = word_subst.get(word)


def save_to_csv(dict_path, dict):
    writer = csv.writer(open(dict_path, 'wb'))
    for key, value in dict.items():
        writer.writerow([key.encode('utf-8'), value.encode('utf-8')])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create good substition dictionary.')
    parser.add_argument('bad_words_path', type=str, help='path to bad words file')
    parser.add_argument('dict_path', type=str, help='path to dictionary')
    args = parser.parse_args()

    if not os.path.isfile(args.bad_words_path):
        print 'Wrong path to bad words file'
        exit()

    read_bad_words(args.bad_words_path)
    make_good_substs()
    save_to_csv(args.dict_path, bad_word_substs)




