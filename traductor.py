#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from litebrowser import Browser
from fileinput import input
import urllib

BASE_URL = ("http://translate.google.com/translate_a/t?"
    "client=t&sl=auto&tl=es&hl=es-419&sc=2&ie=UTF-8&oe=UTF-8&"
    "uptl=es&alttl=en&oc=1&otf=2&ssel=0&tsel=0&q=%s")
b = Browser()
b.go("http://translate.google.com")

for line in input():
    text = urllib.quote(line)
    b.go(BASE_URL % text)
    print b.get_html()
