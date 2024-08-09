import os
import random
import shutil
from distutils.dir_util import copy_tree

dir = './cards/'
discard_pile = './discard_pile'
if len(os.listdir(dir)) == 0:
	print("empty")
else:
	file = random.choice(os.listdir("./last_drawn_card"))
	shutil.move("./last_drawn_card/"+file, "./discard_pile")
	file = random.choice(os.listdir(dir))
	print(file)
	shutil.rmtree("./last_drawn_card")
	os.mkdir("./last_drawn_card")
	shutil.move("./cards/"+file, "./last_drawn_card")


