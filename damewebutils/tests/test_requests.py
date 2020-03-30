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
import requests

class TestRequests(TestCase):

    def test_options(self):
        r = requests.get('https://api.github.com/repos/kennethreitz/requests/issues/482')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.url, 'https://api.github.com/repositories/1362490/issues/482')



    # def test_session2(self):
    #     s = requests.Session()
    #     s.auth = ('user', 'pass')
    #     s.headers.update({'x-test': 'true'})
    #     # both 'x-test' and 'x-test2' are sent
    #     s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
    #     self.assertEqual(s.text, "asdf")
