#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import urllib
import random
import webbrowser
import xml.etree.ElementTree as ET
import httplib

from konlpy.tag import Hannanum
from lxml import html
import pytagcloud # requires Korean font support
import sys

import csv

if len(sys.argv) < 3:
    print("TypeError: not enough arguments.")
    print("python drawWordCloud.py {'keyword'} {count}")
    sys.exit()


if sys.version_info[0] >= 3:
    urlopen = urllib.request.urlopen
else:
    urlopen = urllib.urlopen


r = lambda: random.randint(0,255)
color = lambda: (r(), r(), r())

def get_news_text(query):
    params = urllib.urlencode({'query': query, 'display': 50, 'start': 1})
    headers = {"X-Naver-Client-Id": "TsshNF_3sY3pu9gOkU7d","X-Naver-Client-Secret": "5FOHV3Ysqo"}
    conn = httplib.HTTPSConnection("openapi.naver.com")
    url = '/v1/search/news.xml?query=%s&display=50&start=1&sort=sim' % urllib.quote_plus(query)
    conn.request("GET", url ,params, headers)
    response = conn.getresponse()
    root = ET.fromstring(response.read())
    descriptionTest = ''
    for description in root.iter('description'):
        descriptionTest += description.text
    return descriptionTest


def get_tags(text, ntags=int(sys.argv[2]), multiplier=10):
    h = Hannanum()
    nouns = h.nouns(text)
    count = Counter(nouns)
    return [{ 'color': color(), 'tag': n, 'size': c*multiplier }\
                for n, c in count.most_common(ntags)]

def draw_cloud(tags, filename, fontname='Noto Sans CJK', size=(800, 600)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
    webbrowser.open(filename)

def write_csv(tags, filename):
    with open(filename, 'w') as csvfile:
        fieldnames = ['keyword_name', 'keyword_size']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for tag in tags:
            writer.writerow({'keyword_name': tag['tag'].encode('utf-8'), 'keyword_size': str(tag['size'])})


#pass the arg inputed keyword by user.
query = sys.argv[1]
text = get_news_text(query)
tags = get_tags(text)
print(tags)
write_csv(tags,'wordcloud.csv')
draw_cloud(tags, 'wordcloud.png')