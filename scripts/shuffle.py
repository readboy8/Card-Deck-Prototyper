from distutils.dir_util import copy_tree
import shutil

reference = "./reference_deck"
target = "./deck"

shutil.rmtree(target)
copy_tree(reference, target)
open("./last_drawn_card/placeholder.txt","a")
