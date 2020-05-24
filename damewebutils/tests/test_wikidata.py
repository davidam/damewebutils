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

    def test_surnames(self):
        url = 'https://query.wikidata.org/sparql'
        query = """
SELECT ?surname ?surnameLabel ?count
WHERE
{
  {
    SELECT ?surname (COUNT(?human) AS ?count) WHERE {
    # ?human wdt:P31 wd:Q5.
      ?human wdt:P734 ?surname.
    }
    GROUP BY ?surname ORDER BY DESC(?count) LIMIT 2
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?count)
LIMIT 2
# limit to 10 results so we don't timeout
"""
        r = requests.get(url, params = {'format': 'json', 'query': query})
        data = r.json()
        l = []
        for result in data["results"]["bindings"]:
            elem = [result['surnameLabel']['value'], result['count']['value']]
            l.append(elem[0])
        self.assertEqual(l, ['Li','Wang'])

    def test_openstreetmap(self):
        # https://www.wikidata.org/wiki/Wikidata:OpenStreetMap
        url = 'https://query.wikidata.org/sparql'
        query = """
SELECT ?itemLabel ?item ?OSM ?code
WHERE
{
        ?item wdt:P31 wd:Q6465 . #French départements
        ?item wdt:P300 ?code . #with ISO 3166-2 code
        OPTIONAL { ?item wdt:P402 ?OSM }. #OSM relation if available
        SERVICE wikibase:label { bd:serviceParam wikibase:language "fr" }
}
"""
        r = requests.get(url, params = {'format': 'json', 'query': query})
        data = r.json()
        l = []
        vector = data['results']['bindings'][0]
        values = [vector['code']['value'], vector['OSM']['value'], vector['itemLabel']['value'], vector['item']['value']]
        self.assertEqual(values, ['FR-75', '7444', 'Paris', 'http://www.wikidata.org/entity/Q90'])

    def test_conan_doyle(self):
        # See https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial#Arthur_Conan_Doyle_books
        url = 'https://query.wikidata.org/sparql'
        query = """
SELECT ?book ?bookLabel
WHERE
{
  ?book wdt:P50 wd:Q35610.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
}
ORDER BY DESC(?book)
LIMIT 2

"""
        r = requests.get(url, params = {'format': 'json', 'query': query})
        data = r.json()
#        print(data['results']['bindings'][0]['bookLabel'])
        self.assertEqual(data['results']['bindings'][0]['bookLabel'], {'type': 'literal', 'value': 'Q45192'})
        
 
        
