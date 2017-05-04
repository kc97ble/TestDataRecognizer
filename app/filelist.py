from os import listdir
from os.path import isfile, join, isdir

RESTRICTED_CHARS = "<>:\"/\\|?*"


def is_valid(str):
    for char in str:
        if ord(char) < 32 or ord(char) > 126 or RESTRICTED_CHARS.__contains__(char):
            return False
    return True


class FileList:
    def __init__(self, path):
        if not isdir(path):
            raise AssertionError("Directory does not exist. " + path)
        files = [f for f in listdir(path) if isfile(join(path, f)) and is_valid(f)]
        self.dirs = [f for f in listdir(path) if isdir(join(path, f)) and is_valid(f)]
        for d in self.dirs:
            for f in listdir(join(path, d)):
                if isfile(join(path, d, f)) and is_valid(f):
                    files.append('%s/%s' % (d, f))
        for i in range(len(files)):
            files[i] = files[i].lower()
        files = sorted(files)
        self.files = []
        for i in range(len(files)):
            if (i > 0 and files[i] == files[i - 1]) or (i + 1 < len(files) and files[i] == files[i + 1]):
                pass
            else:
                self.files.append(files[i])
