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
# here starts the stuff that is interesting for you
####################################################

# you only need to import the module
import adba
import threading
from time import time,sleep,strftime,localtime


# lets see the version
print("version: "+str(adba.version))
connection = adba.Connection(log=logwrapper,keepAlive=True)


class ThreadLookUp(threading.Thread):
    
    def __init__(self,animeName):
        super(ThreadLookUp, self).__init__()
        self.animeName = animeName
        self.name = "Thread - "+str(self.animeName)
        print(self.name+" started")
    
    def run(self):
        if not connection.authed():
            log_function("authenticating in thread: "+self.getName())
            if(user and pw):
                connection.auth(user, pw)
        else:
            log_function("no need to authenticate some one else did it")
        
        if(self.animeName != ""):
            anime = adba.Anime(connection,name=self.animeName,paramsA=['aid'])
            anime.load_data()
            log_function("the id to "+self.animeName+" is "+str(anime.aid))
        else:
            log_function("not looking up anything you gave me no anime name");



ThreadLookUp("One Piece").start()
#ThreadLookUp("Bleach").start()
log_function("sleeping 4 min...")
sleep((60*4)+30)
connection.logout() 
connection.lastAuth = time()-1801
connection._keep_alive()


log_function("sleeping 10 min...")
sleep(60*10)
beep()
log_function("sleeping another 10 min...")
sleep(60*10)

beep()
beep()
log_function("checking connection after 20 min")
log_function("connection status: "+str(connection.authed()))

log_function("sleeping another 10 min...")
sleep(60*10)

beep()
beep()
beep()
log_function("checking connection after 30 min")
log_function("connection status: "+str(connection.authed()))
log_function("sleeping another 10 min...")
sleep(60*10)

beep()
beep()
beep()
beep()
print(getNowString()+": checking connection after 40 min")
print(getNowString()+": connection status: "+str(connection.authed()))

print("checking connection with a real request...")
ThreadLookUp("Bleach").start()
