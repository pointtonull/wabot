#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from litebrowser import Browser

b = Browser()
b.go("http://translate.google.com")
b.go("http://translate.google.com/translate_a/t?client=t&sl=auto&tl=es&hl=es-419&sc=2&ie=UTF-8&oe=UTF-8&uptl=es&alttl=en&oc=1&otf=2&ssel=0&tsel=0&q=hi,%20how%20are%20you?")
print b.get_html()
