import os
import shutil

shutil.rmtree("./last_drawn_card")
os.mkdir("./last_drawn_card")
shutil.rmtree("./discard_pile")
os.mkdir("./discard_pile")
