import os
import zipfile
import shutil

def extract_pages(f, p):
	with zipfile.ZipFile(f, 'r') as myzip:
		myzip.extractall(path = p)

def chapter_dir(f, cur_path):
	chap_path = os.path.join(cur_path, f[:-4])
	if not os.path.exists(chap_path):
		os.mkdir(chap_path)
		chap_folders.append(chap_path)
		
def rename_all_pages():
	i = 1
	for folder in chap_folders:
		chap_path = os.path.join(cur_path, folder)
		for names in os.listdir(chap_path):
			os.rename(os.path.join(chap_path, names), os.path.join(chap_path, str(i) + ".jpg"))
			i += 1
			
def move_to_folder():
	name = input("name of folder: ")
	vol_path = os.path.join(cur_path, name)
	if not os.path.exists(vol_path):
		os.mkdir(vol_path)
	for folder in chap_folders:
		chap_path = os.path.join(cur_path, folder)
		for pages in os.listdir(chap_path):
			shutil.move(os.path.join(chap_path, pages), vol_path) 

def delete_chap_folders():
	for names in chap_folders:
		fold_path = os.path.join(cur_path, names)
		os.rmdir(fold_path)

cur_path = os.getcwd()
chap_folders = []

for r, d, f in os.walk(cur_path):
	for files in f:
		if ".zip" in files:
			chap_path = os.path.join(cur_path, files[:-4])
			chapter_dir(files, cur_path)
			extract_pages(files, chap_path)
			
	rename_all_pages()
	move_to_folder()
	delete_chap_folders()
	

