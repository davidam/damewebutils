#!/bin/bash

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

python3 urls.py http://www.davidam.com > files/tests/davidam-index-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/davidam-index.txt files/tests/davidam-index-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "urls.py with davidam.com test is failing"
else
    echo "urls.py with davidam.com test is ok"
fi


python3 imgs.py http://www.damegender.net > files/tests/damegender-imgs-$(date "+%Y-%m-%d-%H").txt

if ! cmp files/tests/damegender-imgs.txt files/tests/damegender-imgs-$(date "+%Y-%m-%d-%H").txt >/dev/null 2>&1
then
    echo "imgs.py with damegender.net test is failing"
else
    echo "imgs.py with damegender.net test is ok"
fi