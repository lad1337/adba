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
from time import time,sleep,strftime,localtime


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

def beep():
    f=open('/dev/tty','w') 
    f.write(chr(7)) 
    f.close() 

def getNowString():
    return strftime("%Y-%m-%d %H:%M:%S", localtime(time())) 

def log_function(data,logLvl="INFO"):
    print(getNowString()+"-"+str(logLvl)+": "+str(data))
logwrapper = lambda x :log_function("anidb: "+str(x),"DEBUG")

