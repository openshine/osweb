#!/usr/bin/python
from django.core.management import execute_manager
import os
import sys
import glob

if os.system("./waf devroot > /dev/null 2>&1") != 0:
    print "Something wrong while try to install devroot"
    print "  * Check the errors with ./wav devroot"
    sys.exit(1)

for p in glob.glob("%s/DEVROOT/usr/lib/python*/site-packages" % os.getcwd()):
    sys.path.insert(0, p)

try:
    import osweb.settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(osweb.settings)
