class FileObject:
  def __init__(self, filename, dirpath, fullpath):
    self.filename = filename
    self.dirpath = dirpath
    self.fullpath = fullpath

class ResultObject:
	def __init__(self, lineFilePath, lineNumber, lineContent):
		self.lineFilePath = lineFilePath
		self.lineNumber = lineNumber
		self.lineContent = lineContent