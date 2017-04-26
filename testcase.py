class TestCase:
    """A pair of two file names

    Attributes:
        inputFile -- file path of input file
        outputFile -- file path of output file
    """

    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile

    def __str__(self):
        return "({}, {})".format(self.inputFile, self.outputFile)


if __name__ == "__main__":
    print TestCase("0.in", "0.ans")
