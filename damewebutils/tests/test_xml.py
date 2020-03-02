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
# along with damewebutils; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from unittest import TestCase
from xml.dom import minidom
import xml.etree.ElementTree as ET

class TestXml(TestCase):

    def test_minidom(self):
        xmldoc = minidom.parse('files/items.xml')
        itemlist = xmldoc.getElementsByTagName('item')
        self.assertEqual(len(itemlist), 4)
        l = []
        for s in itemlist:
            l.append(s.attributes['name'].value)
        self.assertEqual(l, ['item1', 'item2', 'item3', 'item4'])

    def test_et(self):
        tree = ET.parse('files/rss.xml')
        l = []
        for elem in tree.iter():
            l.append(elem)
        self.assertEqual(len(l), 855)

    def test_et_modify(self):
        tree = ET.parse('files/index.xhtml')
        p = tree.find("body/p")
        links = list(p.iter("a"))
        self.assertEqual(2, len(links))
        for i in links:
            i.attrib["target"] = "blank"
        tree.write("files/output.xhtml")
        self.assertNotEqual("files/index.xhtml", "files/output.xhtml")
