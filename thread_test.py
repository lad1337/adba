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
# here starts the stuff that is interesting for you
####################################################

# you only need to import the module
import adba
import threading
import time

# lets see the version
print("version: "+str(adba.version))
connection = adba.Connection(verbos=True)


class ThreadLookUp(threading.Thread):
    
    def __init__(self,animeName):
        super(ThreadLookUp, self).__init__()
        self.animeName = animeName
        self.name = "Thread - "+str(self.animeName)
        print(self.name+" started")
    
    def run(self):
        if not connection.authed():
            print("authenticating in thread: "+self.getName())
            if(user and pw):
                connection.auth(user, pw)
        else:
            print("no need to authenticate some one else did it")
        
        if(self.animeName != ""):
            anime = adba.Anime(connection,name=self.animeName,paramsA=['aid'])
            anime.load_data()
            print("the id to "+self.animeName+" is "+str(anime.aid))
        else:
            print("not looking up anything you gave me no anime name");



ThreadLookUp("One Piece").start()
ThreadLookUp("Bleach").start()


