import urllib2
import argparse
import pymorphy2
from BeautifulSoup import BeautifulSoup
from parser import is_good_link
from db_helper import Helper


link_set = set()
cnt = 0
helper = None
morph = pymorphy2.MorphAnalyzer()


def get_words(tag_content):
    #print tag_content
    for word in tag_content.split(' '):
        if morph.word_is_known(word):
            helper.add(word.lower())


def crawl(page_address, web_site):
    global cnt
    try:
        page = urllib2.urlopen(page_address)
        soup = BeautifulSoup(page)
        for tag in soup.findAll('p'):
            if tag.contents:
                content = tag.contents[0]
                if isinstance(content, basestring):
                    get_words(content)
        for tag in soup.findAll('a'):
            if 'href' in dict(tag.attrs):
                u = tag['href']
                if is_good_link(u, web_site) and u not in link_set:
                    link_set.add(u)
                    cnt += 1
                    if cnt > 5:
                        exit(0)
                    crawl(u, web_site)
        print "ok"
    #except ValueError:
    finally:
        print "value error"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visit and save this page')
    parser.add_argument('db_path', type=str, help='path to database')
    parser.add_argument('inet_path', type=str, help='path to page')

    args = parser.parse_args()
    db_path = args.db_path

    helper = Helper(db_path)
    crawl(args.inet_path, args.inet_path)


