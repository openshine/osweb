# -*- python -*- 

import os
import glob
import fnmatch

VERSION = '0.1'
APPNAME = 'osweb'

top = '.'
out = 'build'

def configure(conf):
    conf.check_tool('python')
    conf.check_tool('gnu_dirs')
    conf.check_python_version((2,7,0))
    conf.define('PYEXECDIR', conf.env["PYTHONDIR"])

    conf.define('VERSION', VERSION)
    
    if conf.env['SYSCONFDIR'] == '/usr/etc':
        conf.define('SYSCONFDIR', '/etc')
    else:
        conf.define('SYSCONFDIR', conf.env['SYSCONFDIR'])

    if conf.env['LOCALSTATEDIR'] == '/usr/var':
        conf.define('LOCALSTATEDIR', '/var')
    else:
        conf.define('LOCALSTATEDIR', conf.env['LOCALSTATEDIR'])

    conf.define('prefix', conf.env["PREFIX"])
    conf.define('PACKAGE', APPNAME)

def options(opt):
    opt.tool_options("python")
    opt.tool_options("gnu_dirs")

def build(bld):
    subdirs_to_add = []
    for f in glob.glob("*/wscript_build"):
        bld.add_subdirs(os.path.dirname(f))
    
    

