from os import walk
import re
import time

from classes import FileObject, ResultObject
# from functions import listFiles, searchInFiles

# Variables globales
filesCount = 0
files = []
linesCount = 0
lines = []

# Fonctions à exporter plus tard
def listFiles(path):
	for (dirpath, dirnames, filenames) in walk(path):
		for filename in filenames:
			if filename.endswith(".txt") :
				files.append(FileObject(filename, dirpath, dirpath + "/" + filename))

def searchInFiles():
	global filesCount
	
	for fobj in files:
		filesCount = filesCount + 1
		print("file:", filesCount, "/", len(files), "/", fobj.fullpath)
		f = open(fobj.fullpath, "r")
		if f.mode == "r":
			print('\n'.join(re.findall('\\w*'+patternInput+'\\S*',f.read())))
			# for line in re.findall('\\w*'+patternInput+'\\S*',f.read()):
			# 	lines.append(ResultObject(fobj.fullpath, "x", line))

userPath = input("Enter a relative path to the parent folder you want to look into ( Or leave blank to search into './' ) : ")
if userPath == "":
	userPath = "./"

patternInput = input("Enter a pattern to look for ( Or leave blank to search for '@gmail' ) : ")
if patternInput == "":
	patternInput = "@gmail"

# ignore = input("Enter an ignore folder filter or leave blank")

startListing = time.time()
print("-----------------------------------------------")
print("listing all files in \"" + userPath + "\" ")

listFiles(userPath)

print("-----------", len(files), "files in the list --------------")
endListing = time.time()
print("Listing execution time :", endListing - startListing)
print("-----------------------------------------------")


startSearching = time.time()
print("-----------------------------------------------")
print("---------- Search results ----------")
print("-----------------------------------------------")

searchInFiles()

print("-----------------------------------------------")
# print(results, "lines in the list")
endSearching = time.time()
print("Searching execution time :", endSearching - startSearching)
print("-----------------------------------------------")
