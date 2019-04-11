from os import walk
import re
import time

from classes import FileObject, ResultObject
# from functions import listFiles, searchInFiles

# Fonctions à exporter plus tard
def listFiles(path):
	for (dirpath, dirnames, filenames) in walk(path):
		for filename in filenames:
			if filename.endswith(".txt") :
				files.append(FileObject(filename, dirpath, dirpath + "/" + filename))

def searchInFiles():
	count = 0
	for fobj in files:
		count = count + 1
		print("file:", count, "/", len(files))
		# with open(fobj.fullpath, encoding="UTF-8") as f:
		# with open(fobj.fullpath, encoding="ISO-8859-1") as f:
		f = open(fobj.fullpath, "r")
		if f.mode == "r":
			print('\n'.join(re.findall('\\w*'+patternInput+'\\S*',f.read())))

		# Ancienne methode de recuperation (separée par \n)
		# with open(fobj.fullpath, "r",-1,"UTF-8") as f:
		# with open(fobj.fullpath, "r") as f:
		# 	for line in f.readlines():
		# 		if re.search(patternInput, line):
		# 				lines.append(ResultObject(fobj.fullpath, "x", line))
		# 				# print(fobj.fullpath, " / ", line)

userPath = input("Enter a relative path to the parent folder you want to look into ( Or leave blank to search into './' ) : ")
if userPath == "":
	userPath = "./"

patternInput = input("Enter a pattern to look for ( Or leave blank to search for '@gmail' ) : ")
if patternInput == "":
	patternInput = "@gmail"

# ignore = input("Enter an ignore folder filter or leave blank")

files = []
lines = []

startListing = time.time()

print("-----------------------------------------------")
print("---------- listing all files in \"" + userPath + "\" ----------")

listFiles(userPath)

print("-----------", len(files), "files in the list --------------")
endListing = time.time()
print("Listing execution time :", endListing - startListing)
print("-----------------------------------------------")

# doSearchString = "Search \"" + doSearchPattern + "\" in all files ? (type 'y' for yes or anything else for no) : "
doSearch = "y"
# doSearch = input(doSearchString)

if doSearch == "y":
	startSearching = time.time()

	print("-----------------------------------------------")
	print("---------- Search results ----------")
	print("-----------------------------------------------")

	searchInFiles()
	for line in lines:
		print(line.lineFilePath, " / ", line.lineContent)

	print("-----------------------------------------------")
	print("-----------", len(lines), "lines in the list --------------")
	endSearching = time.time()
	print("Searching execution time :", endSearching - startSearching)
	print("-----------------------------------------------")
