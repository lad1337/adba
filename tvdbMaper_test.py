#!/usr/bin/env python
#
# This file is part of aDBa.
#
# aDBa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# aDBa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with aDBa.  If not, see <http://www.gnu.org/licenses/>.
import sys
import os
import getopt
from test_lib import *
import threading 

####################################################
# here starts the stuff that is interesting for you
####################################################

# you only need to import the module
import adba

print("--- test with name ---")
anime = adba.Anime(None,name="Ao no Exorcist");
print "tvdb_id:",anime.tvdb_id
print "anidb_id:",anime.aid

print("--- test with aid ---")
anime = adba.Anime(None,aid=8148);
print "tvdb_id:",anime.tvdb_id
print "name:",anime.name

print("--- test with tvdbid ---")
anime = adba.Anime(None,tvdb_id=248035);
print "anidb_id:",anime.aid
print "name:",anime.name