from os import walk
import sys
import re
import time

class FileObject:
  def __init__(self, filename, dirpath, fullpath):
    self.filename = filename
    self.dirpath = dirpath
    self.fullpath = fullpath

class ErrorObject:
  def __init__(self, errorType, message):
    self.errorType = errorType
    self.message = message

files = []
linesCount = 0
errors = []

def listFiles(path):
	for (dirpath, dirnames, filenames) in walk(path):
		for filename in filenames:
			try:
				if filename.endswith(".txt") or filename.endswith(".sql"):
					files.append(FileObject(filename, dirpath, dirpath + "/" + filename))
			except:
				errors.append(ErrorObject("ListFiles() Error", "An error occured while looking through the directories/files" + fobj.fullpath))

def searchInFiles():
	filesCount = 0
	filesLength = len(files)
	
	for fobj in files:
		try:
			filesCount = filesCount + 1
			print("file:", filesCount, "/", filesLength, "|| percentage: ", int(filesCount * 100 / filesLength), "% || results: ", linesCount)

			f = open(fobj.fullpath, "r")
			# f = open(fobj.fullpath, "rb",-1,"UTF-8")
			if f.mode == "r":
				print('\n'.join(re.findall('\\w*'+patternInput+'\\S*',f.read())))

		except:
			errors.append(ErrorObject("searchInFiles() Error", "An error occured while opening or reading the file" + fobj.fullpath))
		finally:
			f.close()


userPath = input("Enter a relative path to the parent folder you want to look into ( Or leave blank to search into './' ) : ")
if userPath == "":
	userPath = "./"

patternInput = input("Enter a pattern to look for ( Or leave blank to search for '@gmail' ) : ")
if patternInput == "":
	patternInput = "@gmail"

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
endSearching = time.time()
print("Searching execution time :", endSearching - startSearching)
print("Number of registered lines : ", linesCount)
print("-----------------------------------------------")

printErrors = input("Do you want to see the", len(errors),"execution errors ? ( enter 'yes' or 'y' ) : ")
if printErrors == "y" or printErrors == "yes":
	for error in errors:
		print(error.errorType)
		print(error.message)
	print("Number of registered errors : ", len(errors))
	print("-----------------------------------------------")