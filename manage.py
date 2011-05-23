#!/usr/bin/python

#osweb. Main Openshines website 
#Copyright (C) 2011  Openshine sl
# Authors:
#    Pablo Vieytes <pvieytes@openshine.com>
#    Roberto Majadas <roberto.majadas@openshine.com>
#    Cesar Garcia Tapia <cesar.garcia.tapia@openshine.com>
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.



from django.core.management import execute_manager
import os
import sys
import glob

root = os.path.dirname(os.path.abspath(__file__))
waf_cmd = os.path.join(root, "waf")
root_wscript = os.path.join(root, "wscript")

APPNAME = ''

with open(root_wscript, 'r') as f :
    for line in f.readlines():
        if line.startswith("APPNAME") :
            exec(line)

if APPNAME == '' :
    print "No APPNAME defined in %s" % root_wscript
    sys.exit(1)

if os.system("cd %s && %s devroot" % (root,waf_cmd)) != 0:
    print "Something wrong while try to install devroot"
    print "  * Check the errors with ./wav devroot"
    sys.exit(1)

for p in glob.glob("%s/DEVROOT/usr/lib/python*/site-packages" % root):
    sys.path.insert(0, p)

try:
    exec("import %s.settings" % APPNAME) # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    exec("execute_manager(%s.settings)" % APPNAME)
