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
####################################################
# here starts the stuff that is interresting for you
####################################################

# you only need to import the module
import adba

# lets see the version
print adba.version

# make a connection object
# log = True great for testing not so great for a running system (default is False)
connection = adba.Connection(log=True)

# we can always ping to see if we can reach the server
try:
    connection.ping()
except Exception,e :
    print("exception msg: "+str(e))
    print "if we cant even ping stop right here"
    exit()

# ok lets try to authenticate. we need username and pw for that
try:
    connection.auth(user, pw)
    pass
except Exception,e :
    print("exception msg: "+str(e))

animeList =  ["Bleach", "Naruto Shippuuden", "Blue Exorcist"]
animeList =  ["sdadasda"]


for animeName in animeList:
    print("########################### "+animeName+" ###########################")
    anime = adba.Anime(connection,name=animeName,paramsA=['aid'],load=True)
    groups = anime.get_groups()
    for group in groups:
        print(u"- "+group)

