#!/usr/bin/env python
# coding=utf-8
import requests
import sys
from threading import Thread

content = ''
if len(sys.argv) > 1:
    content = str(sys.argv[1])
else:
    content = str(raw_input('[*]Message: '))


data = {
    'pid':'14',
    'mask':'c0hb1rd',
    'content':content
}

url = 'http://addons.bbdfun.com/TreeHole/Index/sendArticle'

def main(judge):
#    print '\n[*]Starting NO.', judge
    requests.post(url, data=data)
    print '[*]Success NO.', judge

for i in range(1, 11):
    Thread(target=main, args=(i,)).start()

