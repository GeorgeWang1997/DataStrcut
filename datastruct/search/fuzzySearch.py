# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: fuzzySearch.py
@time: 2019-04-13 16:34
"""

import re


def fuzzy_search(input, collection, accessor=lambda x: x):

    suggestions = []
    input = str(input) if not isinstance(input, str) else input
    pat = '.*?'.join(map(re.escape, input))
    regex = re.compile(pat)
    for item in collection:
        r = regex.search(accessor(item))
        if r:
            suggestions.append((len(r.group()), r.start(), accessor(item), item))

    return (z[-1] for z in sorted(suggestions))
