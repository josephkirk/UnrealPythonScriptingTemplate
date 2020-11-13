import unreal
from os.path import dirname, basename, isfile, join
import glob
import importlib

dir_name = dirname(__file__)
dir_basename = basename(dir_name)
modules = glob.glob(join(dir_name, "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

unreal.log("""@

####################

Load User Interface

####################
""")

for m in __all__:
    # __import__(m, locals(), globals())
    try:
        importlib.import_module("{}.{}".format(dir_basename, m))
        command = 'import {mod};reload({mod})'.format(mod=m)
        # unreal.log(command)
        exec(command)
        unreal.log("Successfully import {}".format(m))
    except Exception as why:
        unreal.log_error("Fail to import {}\n{}".format(m, why))


unreal.log("""@

####################
""")