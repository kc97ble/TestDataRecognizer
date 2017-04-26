# File list
___________

## Definition of the "file list"

- A _worth-considering file_ is a file which is either
  + directly inside the _given directory_, or
  + directly inside a direct subdirectory of the _given directory_.

- The _relative path_ of a _worth-considering file_ F is defined as follows:
  + If F is directly inside the _given directory_, the _relative path_ of F is defined to be the file name of F.
  + Otherwise, the _relative path_ of F is a string with format `dir name/file name.ext`, where `dir name` is the directory name of the parent directory of F, and `file name.ext` is the file name of F. Note that a slash is used regardless which OS is used.

  For example, let the _given directory_ be `D:\big`:
  + The _relative path_ of `D:\big\dog.txt` is `dog.txt`.
  + The _relative path_ of `D:\big\white\cat.txt` is `white/cat.txt`.

- A _relative path_ is considered to be valid iff
  + it contains only ASCII characters from #32 (space) to #126 ('~'), and
  + it does not contain any of the following characters `< > : " / \ | ? *` (note that space is not a restricted character).

- The _file list_ is the **sorted** list of _relative paths_ of all the _worth-considering files_, after removing invalid _relative paths_.

### Example 1

Let the _given directory_ be `D:\Problems 2017\ascii`. Additionally, suppose that all the files inside the _given directory_ are:
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
1/ascii.in
1/ascii.ans
2/ascii.in
2/ascii.ans
README
statement.pdf
```

Note that file "index.html" is too "deep", and the file name of the last file contains non-ASCII characters.

