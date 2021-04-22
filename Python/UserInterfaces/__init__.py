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

Load UI Library 

####################
""")

for m in __all__:
    # __import__(m, locals(), globals())
    try:
        mod = importlib.import_module("{}.{}".format(dir_basename, m))
        try:
            reload(mod)
        except:
            importlib.reload(mod)
        unreal.log("Successfully import {}".format(m))
    except:
        unreal.log_error("Fail to import {}".format(m))


unreal.log("""@

####################
""")