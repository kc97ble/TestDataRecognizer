from testcase import *

class Spec:
	
	def __init__(self, inputSpec, outputSpec, specType):
		self.inputSpec = inputSpec
		self.outputSpec = outputSpec
		self.specType = specType
	
	def __str__(self):
		return "({}, {}, {})".format(self.inputSpec,
			self.outputSpec, self.specType)

	def match_suffix(self, testCase):
		return testCase.inputFile.endswith(self.inputSpec)\
			and testCase.outputFile.endswith(self.outputSpec)\
			and ...

	def match_prefix(self, testCase):
		return testCase.inputFile.startswith(self.inputSpec)\
			and testCase.outputFile.startswith(self.outputSpec)\
			and ...
	
	def match(self, testCase):
		if self.specType=='$':
			return self.match_suffix(testCase)
		if self.specType=='^':
			return self.match_prefix(testCase)
		raise AssertionError("specType muse be '$' or '^'")

if __name__ == "__main__":
	print Spec(".in", ".ans", '$')
	print TestCase("1.in", "1.ans")
	print Spec(".in", ".ans", '$').match(TestCase("1.in", "1.ans"))
	
		
