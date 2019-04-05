from os import walk
path ="./"
directories = []
files = []

class FileObject:
  def __init__(self, directory, filename, fullpath):
    self.directory = directory
    self.filename = filename
    self.fullpath = fullpath

for (dirpath, dirnames, filenames) in walk(path):
    # for directory in dirnames:
    #     directories.append(os.path.join(root, directory))
    #     print os.path.join(root, directory) 
    for filename in filenames: 
        # files.append(FileObject(os.path.join(root, directory), os.path.join(root,filename), os.path.join(root, directory) + os.path.join(root,filename) ))
        print (path.join(dirpath,filename))

