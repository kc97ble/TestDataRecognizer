class TestCase:
    """A pair of two file names

    Attributes:
        inputFile -- file path of input file
        outputFile -- file path of output file
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def __str__(self):
        return "({}, {})".format(self.input_file, self.output_file)


if __name__ == "__main__":
    print TestCase("0.in", "0.ans")
