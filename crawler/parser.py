# -*- coding: utf8 -*-

import re


def is_good_link(link, base):
    if base.endswith('tjournal.ru/'):
        if re.match('^' + base + '[0-9]+.*', link) and 'comment' not in link :
            return True
        else:
            return False
    if base.endswith('vc.ru/'):
        if link.startswith(base + 'p/') and 'comment' not in link:
            return True
        else:
            return False
