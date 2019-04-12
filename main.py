from os import walk
import sys
import re
import time

from classes import FileObject, ResultObject, ErrorObject
# from functions import listFiles, searchInFiles

# Variables globales
filesCount = 0
files = []
linesCount = 0
lines = []

errors = []

# Fonctions à exporter plus tard
def listFiles(path):
	for (dirpath, dirnames, filenames) in walk(path):
		for filename in filenames:
			try:
				if filename.endswith(".txt"):
					files.append(FileObject(filename, dirpath, dirpath + "/" + filename))
			except:
				errors.append(ErrorObject("ListFiles Error", "An error occured while looking through the directories/files" + fobj.fullpath))

def searchInFiles():
	global filesCount
	
	for fobj in files:
		try:
			filesCount = filesCount + 1
			print("file:", filesCount, "/", len(files), "/", int(filesCount * 100 / len(files)), "%")
			# sys.stdout.write("".join(["Progression :", str(int(filesCount * 100 / len(files))), "%"]))
			# sys.stdout.flush()
			# print("Progression :", int(filesCount * 100 / len(files)), "%", end="\r")
			f = open(fobj.fullpath, "r")
			# f = open(fobj.fullpath, "r",-1,"UTF-8")
			if f.mode == "r":
				# print('\n'.join(re.findall('\\w*'+patternInput+'\\S*',f.read())))
				for line in re.findall('\\w*'+patternInput+'\\S*',f.read()):
					lines.append(ResultObject(fobj.fullpath, "x", line))
					print(line)
			f.close()
		except:
			errors.append(ErrorObject("searchInFiles Error", "An error occured while opening or reading the file" + fobj.fullpath))


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
print("Number of registered lines : ", len(lines))
print("-----------------------------------------------")

printlines = input("Do you want to see a récap of the results résults ? ( enter 'yes' or 'y' to print them ) : ")
if printlines == "y" or printlines == "yes":
	for line in lines:
		print(line.lineContent)
	print("Number of registered lines : ", len(lines))
	print("-----------------------------------------------")

printErrors = input("Do you want to see the execution errors ? ( enter 'yes' or 'y' to print them ) : ")
if printErrors == "y" or printErrors == "yes":
	for error in errors:
		print(error.errorType)
		print(error.message)
	print("Number of registered errors : ", len(errors))
	print("-----------------------------------------------")