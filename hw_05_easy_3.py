import os
import shutil
import sys

path = sys.argv[0]
name = os.path.basename(sys.argv[0])
shutil.copyfile(path, path[:len(path) - len(name)] + 'new_' + name)
