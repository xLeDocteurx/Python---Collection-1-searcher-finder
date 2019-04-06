from os import walk
import re
# from "./classes.py" import FileObject

patternInput = "@hotmail.com"
userPath = "./"
# ignore = [
# 		".git",
# 	]
ignore = ".git"

files = []
lines = []

class FileObject:
  def __init__(self, filename, dirpath, fullpath):
    self.filename = filename
    self.dirpath = dirpath
    self.fullpath = fullpath

class ResultObject:
	def __init__(self, lineNumber, lineContent):
		self.lineNumber = lineNumber
		self.lineContent = lineContent

def listFiles(path):
	for (dirpath, dirnames, filenames) in walk(path):
		# # print("Fichiers présent dans le dossier : \"" + dirpath + "\"")
		# for dirname in dirnames:
		for filename in filenames:
			# if dirname != ignore:
			# 	files.append(FileObject(filename, dirpath, dirpath + "/" + filename))
			#	print(dirpath + filename)
			files.append(FileObject(filename, dirpath, dirpath + "/" + filename))

			# # print("Dossiers présent dans le dossier : \"" + dirpath + "\"")
			# # print(dirnames)

def searchInFiles():
	for fobj in files:
		with open(fobj.fullpath, 'r') as f:
			lines = f.readlines()
			for line in lines:
					# if re.search(r'some_pattern', line):
					if re.search(patternInput, line):
							lines.append(line)
							break

print("-----------------------------------------------")
print("---------- listing all files in \"" + userPath + "\" ----------")
print("-----------------------------------------------")

listFiles(userPath)

for fobj in files:
	print(fobj.fullpath)

print("-----------------------------------------------")
print("-----------", len(files), "items in the list --------------")
print("-----------------------------------------------")

print("-----------------------------------------------")
print("---------- Search results ----------")
print("-----------------------------------------------")

searchInFiles()

for line in lines:
	print(line)

print("-----------------------------------------------")
print("---------- listing all files in \"" + userPath + "\" ----------")
print("-----------------------------------------------")
