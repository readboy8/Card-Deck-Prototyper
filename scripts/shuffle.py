from distutils.dir_util import copy_tree
import shutil

reference = "./reference_deck"
target = "./cards"

shutil.rmtree(target)
copy_tree(reference, target)
