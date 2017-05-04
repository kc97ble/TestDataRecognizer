from app.filelist import FileList
import os, unittest, pytest


class CheckFileList(unittest.TestCase):
    def setUp(self):
        self.dir = os.path.join(os.getcwd(), 'checks', 'sample_filelist', 'ascii')
        self.wrong_dir = self.dir + 's'

    def test_init(self):
        with pytest.raises(AssertionError) as excinfo:
            fl1 = FileList(self.wrong_dir)
        assert "Directory does not exist." in str(excinfo.value)

        fl2 = FileList(self.dir)
        assert [f for f in fl2.files if f[0] != '.'] == [
            '1/ascii.ans',
            '1/ascii.in',
            '2/ascii.ans',
            '2/ascii.in',
            'readme',
            'statement.pdf',
        ]
