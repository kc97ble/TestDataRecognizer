class TestCase:
    """A pair of two file names

    Attributes:
        input_file -- file path of input file
        output_file -- file path of output file
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def __str__(self):
        return "({}, {})".format(self.input_file, self.output_file)
