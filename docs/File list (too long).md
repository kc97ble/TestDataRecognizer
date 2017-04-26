# File list
___________

## Definition of the "file list"

### Definition of a "worth-considering file"

- A _worth-considering file_ is a file which is either
  + directly inside the _given directory_, or
  + directly inside a direct subdirectory of the _given directory_.

### Definition of a "relative path" of a "worth-considering file"

- The _relative path_ of a _worth-considering file_ F is defined as follows:
  + If F is directly inside the _given directory_, the _relative path_ of F is defined to be the file name of F.
  + Otherwise, the _relative path_ of F is made by concatenating these strings:
    * The directory name of the parent of F
    * A slash ('/'), regardless which OS is used
    * The file name of F

  For example, let the _given directory_ be `/tmp`:
  + The _relative path_ of `/tmp/dog.txt` is `dog.txt`.
  + The _relative path_ of `/tmp/big/white cat.txt` is `big/white cat.txt`.

  Slashes are used in a _relative path_ even on Windows. For example, let the _given directory_ be `D:\big`:
  + The _relative path_ of `D:\big\dog.txt` is `dog.txt`.
  + The _relative path_ of `D:\big\white\cat.txt` is `white/cat.txt`.

### Validity of a "relative path"

- A _relative path_ is considered to be valid iff
  + it contains only ASCII characters from #32 (space) to #126 ('~'), and
  + it does not contain any of the following characters `< > : " / \ | ? *` (note that space is not a restricted character).

### Definition of the "file list"

- The _file list_ is the **sorted** list of _relative paths_ of all the _worth-considering files_, after removing invalid _relative paths_.

- In other words, the _file list_ can be produced by the following algorithm:
  + Let A be the list of all _worth-considering files_.
  + Let B be the list of _relative paths_ of all the files in A.
  + Let C be the list of all valid _relative paths_ in B.
  + Let D be the sorted list of C.
  + Then, the _file list_ is defined to be D.

In the other words, the _file list_ contains all the file inside the _given directory_. Each element has format `filename.ext` or `dirname/filename.ext`. Elements which contains non-valid characters are excluded.

#### Example 1

In this example, let the _given directory_ be
`D:\Problems 2017\ascii`

Assume the list of full paths of all the files inside the _given directory_ is
```
D:\Problems 2017\ascii\README
D:\Problems 2017\ascii\statement.pdf
D:\Problems 2017\ascii\1\ascii.in
D:\Problems 2017\ascii\1\ascii.ans
D:\Problems 2017\ascii\2\ascii.in
D:\Problems 2017\ascii\2\ascii.ans
D:\Problems 2017\ascii\doc\html\index.html
D:\Problems 2017\ascii\xin chào.txt
```

The _file list_ will be:
```
README
statement.pdf
1/ascii.in
1/ascii.ans
2/ascii.in
2/ascii.ans
```

Note that the depth of file "index.html" is to big, and the file name of the last file contains non-ASCII characters.
