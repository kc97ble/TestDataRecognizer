import sys

class TestList:
	"""
	
	"""
	def __init__(self, testCaseList, spec):
		self.testCaseList = testCaseList
		self.spec = spec
		

if __name__ == "__main__":
	"""
	Input: a list of file names.
	Output: the best test list.
	
	Assumptions: Each file name contains only a-z, 0-9, /
	"""
	FileList = []
	for line in sys.stdin:
		FileList.append(line)
	FileList.sort()
	
