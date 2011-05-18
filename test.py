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

opts, extraparams = getopt.getopt(sys.argv[1:],'u:p:f:') 
user = ""
pw = ""
filePath = ""

for o,p in opts:
    if o == '-u':
        user = p
    elif o == '-p':
        pw = p
    elif o == '-f':
        filePath = os.path.abspath(p)
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
# we create an Episode with:
# file: path the file we would like to identify
# paramsF: info we want from the file. for a full list look at adba.maper.aniDBMaper.AniDBMaper.getFileMapF
# paramsA: info we want from the anime. for a full list look at adba.maper.aniDBMaper.AniDBMaper.getFileMapA
# for all params: the order is irrelevant
episode = adba.Episode(connection,filePath=filePath,
     paramsF=["quality","anidb_file_name","crc32"],
     paramsA=["epno","english_name","other_name"])


if connection.authed():
    # we now got an object that holds the info we have and the info we want
    # lets try get the data from the server
    try:
        print("Trying to lookup "+str(filePath)+" on anidb")
        # simply call load_data()
        episode.load_data()
    except Exception,e :
        print("exception msg: "+str(e))


# lets see if we got some valid info
# every thing you asked for will be available as a attribute of the object
# e.g. we asked for "epno" this will be available as episode.epno
# as default you will get None from a attribute

#this is why i check if anidb_file_name is something before i go on
if episode.anidb_file_name:
    # every data should be in the correct type ... list are list numbers are int and so on
    print("Lookup successful, the anidb filename is: "+str(episode.anidb_file_name))

# we are done we have our info in the episode object so lets logout
connection.logout()

# the connection has a thread connected to a socket to stop the tread and free the socket we can call
connection.close()
# this the socket might not be free right away
# ps calling connection.logout(True) would achieve the same