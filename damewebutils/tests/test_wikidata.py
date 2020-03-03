#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

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
from SPARQLWrapper import SPARQLWrapper, JSON
import requests

class TestWikidata(TestCase):

    def test_dbpedia_asturias(self):
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
""")
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        l = []
        for result in results["results"]["bindings"]:
            l.append(result["label"]["value"])
        self.assertEqual(l, ['Asturias', 'منطقة أستورياس', 'Asturien', 'Asturias', 'Asturies', 'Asturie', 'アストゥリアス州', 'Asturië (regio)', 'Asturia', 'Astúrias', 'Астурия', '阿斯图里亚斯'])
