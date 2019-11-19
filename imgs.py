#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with damewebutils; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import requests
from lxml import html
from pprint import pprint
import os,re

start_url = 'http://127.0.0.1:5000'
pages = ['/index.html', '/elisp-es.html', '/org-mode.html', '/gcc.html', '/r.html', '/python.html', '/bash.html', '/vim.html', '/debian.html', '/gimp.html', '/acerca.html', '/libros.html', '/perspectiva-libertaria.html', '/faq-freedoc.html']


for p in pages:
    response = requests.get(start_url + p)
    tree = html.fromstring(response.text)
    imgs = tree.cssselect('img')  # or tree.xpath('//a')

    out = []
    for i in imgs:
    # we use this if just in case some <a> tags lack an href attribute
        if 'src' in i.attrib:
            out.append(i.attrib['src'])

    absoluteurls = []
    for o in out:
        if 'http' in o:
            absoluteurls.append(o)
        else:
            o = start_url + o
            absoluteurls.append(o)

    buggyurls = []
    for l in absoluteurls:
        print(l)
        try:
            r = requests.get(l)
            r.raise_for_status()
            print(r.status_code)
        except:
            buggyurls.append(l)
            print("Error %s" % r.status.code)
    print("Imgs with possible troubles in %s" % l)
#    print(buggyurls)
