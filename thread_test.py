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
from time import time, sleep, strftime, localtime


# lets see the version
print("version: " + str(adba.version))
connection = adba.Connection(log=logwrapper, keepAlive=True)


class ThreadLookUp(threading.Thread):

    def __init__(self, animeName, index):
        super(ThreadLookUp, self).__init__()
        self.animeName = animeName
        self.name = "Thread - " + str(self.animeName) + " - " + str(index)
        print(self.name + " started")

    def run(self):
        if not connection.authed():
            log_function("authenticating in thread: " + self.getName())
            if(user and pw):
                connection.auth(user, pw)
        else:
            log_function(self.name + "no need to authenticate some one else did it")

        if(self.animeName != ""):
            anime = adba.Anime(connection, name=self.animeName, paramsA=['aid'])
            anime.load_data()
            log_function("the id to " + self.animeName + " is " + str(anime.aid))
        else:
            log_function("not looking up anything you gave me no anime name")

sleepTime = 0
threadCount = 3 # this one(none demon), the link that holds the socket(demon) and the connection if keept alive (demon)
print("#####################################")
print("STRESS TEST !!!!1")
print("#####################################")

print("#####################################")
print("Block ONE 8 Threads")
print("#####################################")

for x in range(2):
    for a in ["one piece", "bleach", "Cowboy Bebop", "Usagi Drop"]:
        ThreadLookUp(a, x).start()

while threading.activeCount() > threadCount:
    print "running", threading.activeCount()
    sleep(3)

beep()
beep()
print("#####################################")
print("Wait 3 min. we should see some auto checks / pings")
print("#####################################")
sleep(60*3)
beep()
beep()
print("#####################################")
print("Breaking the session")
print("#####################################")
connection.link.session = None

print("#####################################")
print("Block TWO 8 Threads")
print("#####################################")

for x in range(2):
    for a in ["one piece", "bleach", "Cowboy Bebop", "Usagi Drop"]:
        ThreadLookUp(a, x).start()

while threading.activeCount() > threadCount:
    print "running", threading.activeCount()
    if threading.activeCount() < threadCount + 3:
        print("#####################################")
        print("Just for the hell of it authenticate while some threads run")
        print("#####################################")
        connection.auth(user, pw)
    sleep(3)


print("final logout: " + str(connection.logout()))
print("#####################################")
print("Thank you! Thread / Stress completed!")
print("#####################################")

exit()
