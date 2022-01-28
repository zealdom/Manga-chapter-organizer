import os 
import shutil

cur_path = os.getcwd()
i = 1
folderName = []
for files in os.listdir(cur_path):
	chap_path = os.path.join(cur_path, files)
	if files not in "rename_pages from chfolder.py":
		folderName.append(files)
		for images in os.listdir(chap_path): 
			if ".jpg" in images:
				shutil.move(os.path.join(chap_path, images), cur_path)
				os.rename(os.path.join(cur_path, images), os.path.join(cur_path, str(i)+".jpg"))
				i += 1
for fold in folderName:
	os.rmdir(os.path.join(cur_path, fold))
