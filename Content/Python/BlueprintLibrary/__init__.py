import unreal
from os.path import dirname, basename, isfile, join
import glob
import importlib
import traceback
import sys

dir_name = dirname(__file__)
dir_basename = basename(dir_name)
modules = glob.glob(join(dir_name, "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

unreal.log("""@

####################

Load Blueprint Library 

####################
""")

for m in __all__:
    # __import__(m, locals(), globals())
    try:
        mod = importlib.import_module("{}.{}".format(dir_basename, m))
        if m in globals():
            unreal.log("""@
            ####################

            ReLoad Blueprint Library 

            ####################
            """)
            try:
                reload(mod)
            except:
                importlib.reload(mod)
            # try:
            #     unreal.reload(mod)
            # except:
            #     unreal.log("{} is not Unreal Generated Class".format(m))

        unreal.log("Successfully import {}".format(m))
    except Exception as why:
        unreal.log_error("Fail to import {}.\n {}".format(m, why))
        traceback.print_exc(file=sys.stdout)

unreal.log("""@

####################
""")
