# -*- python -*- 

import os
import glob
import fnmatch

VERSION = '0.0'
APPNAME = 'osweb'

top = '.'
out = 'build'

def configure(conf):
    conf.check_tool('python')
    conf.check_tool('gnu_dirs')
    conf.check_python_version((2,6,0))
    conf.define('PYEXECDIR', conf.env["PYTHONDIR"])

    conf.define('VERSION', VERSION)
    
    conf.define('prefix', conf.env["PREFIX"])
    conf.define('PACKAGE', APPNAME)

def options(opt):
    opt.tool_options("python")
    opt.tool_options("gnu_dirs")

def build(bld):
    subdirs_to_add = []
    for f in glob.glob("*/wscript_build"):
        bld.add_subdirs(os.path.dirname(f))

def dist(ctx):
    ctx.excl = ' **/.waf-1* **/*~ **/*.pyc **/*.swp **/.lock-w* **/debian/* **/.git/* **/.gitignore' 

def devroot(ctx):
    pwd = os.getcwd()
    prefix = os.path.join(os.getcwd(), "DEVROOT", "usr")
    etc = os.path.join(os.getcwd(), "DEVROOT", "etc")
    var = os.path.join(os.getcwd(), "DEVROOT", "var")
    
    conf_cmd = "./waf configure --prefix=%s \
--sysconfdir=%s --localstatedir=%s" % (prefix, etc, var)

    if os.system(conf_cmd) != 0 :
        sys.exit(1)

    if os.system("./waf build") != 0:
        sys.exit(1)
    
    if os.system("./waf install > /dev/null 2>&1") != 0:
        sys.exit(1)
    
    print "------------------------------"
