import os
import shutil

Path = r"C:\Users\qin\AppData\Local\bohaoo\jsb.sqlite"

if os.path.exists(Path):
	shutil.rmtree(Path)
