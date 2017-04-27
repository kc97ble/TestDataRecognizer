# File list
___________

## Definition of the "file list"

- A _worth-considering file_ is a file which is either
  + directly inside the _given directory_, or
  + directly inside a direct subdirectory of the _given directory_.

- The _relative path_ of a _worth-considering file_ F is defined as follows:
  + If F is directly inside the _given directory_, the _relative path_ of F is defined to be `lowercase(filename(F))`.
  + Otherwise, assume that D is the parent directory of F, the _relative path_ of F is defined to be `lowercase(dirname(D)) + '/' + lowercase(filename(F))` where '+' is the concatenation operator.

  For example, let the _given directory_ be `D:\Big`:
  + The _relative path_ of `D:\Big\Dog.txt` is `dog.txt`.
  + The _relative path_ of `D:\Big\White\cat.txt` is `white/cat.txt`.

- A _relative path_ is considered to be valid iff
  + it contains only ASCII characters from #32 (space) to #126 ('~'), and
  + it does not contain any of the following characters `< > : " / \ | ? *` (note that space is not a restricted character), and
  + it is a _relative path_ of **exactly one** _worth-considering file_.

- The _file list_ is the **sorted** list of _relative paths_ of all the _worth-considering files_, after removing all invalid _relative paths_.

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
1/ascii.ans
1/ascii.in
2/ascii.ans
2/ascii.in
readme
statement.pdf
```

Note that "index.html" is not a _worth-considering file_ because it is too "deep", "ascii/xin chào.txt" is not a valid _relative path_ because it contains a non-ASCII character.

## Properties of the "file list"

- It is sorted.
- Its elements are lowercase.
- It only involves files with depth 1 or 2.
- Invalid _relative paths_ are not included in the _file list_.
- Slashes are always used as a directory separator regardless of OS.
- Each element contains only ASCII charaters from #32 to #126, except some restricted characters.
- In a directory, if there exists two different files having the same name (case-insensitively), both files are not included in the _file list_. In general, if `relative_path(F1) == relative_path(F2)`, both F1 and F2 are not included in the _file list_.

