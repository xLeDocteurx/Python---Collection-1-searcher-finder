from os import walk
# from "./classes.py" import FileObject

path ="./"
# ignore = [
# 		".git",
# 	]
ignore = ".git"

files = []

class FileObject:
  def __init__(self, filename, dirpath, fullpath):
    self.filename = filename
    self.dirpath = dirpath
    self.fullpath = fullpath

for (dirpath, dirnames, filenames) in walk(path):
	# # print("Fichiers présent dans le dossier : \"" + dirpath + "\"")
	# for dirname in dirnames:
	# 	print("Nous allons : " + dirname)
	for filename in filenames:
		# if dirname != ignore:
		files.append(FileObject(filename, dirpath, dirpath + "/" + filename))
		# print(dirpath + filename)
		# # print(filename)
	
	# # print("Dossiers présent dans le dossier : " + dirpath)
	# # print(dirnames)


print("-----------------------------------------------")
print("---------- listing all files in \"" + path + "\" ----------")
print("-----------------------------------------------")

for fobj in files:
	print(fobj.fullpath)

print("-----------------------------------------------")
print("-----------", len(files), "items in the list --------------")
print("-----------------------------------------------")
