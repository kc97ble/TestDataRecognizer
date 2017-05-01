# Definitions

## Definition of the "given directory"

- The _given directory_ is the directory in the input.

## Definition of the "file list"

Read `File list.md` for the correct definition of the _file list_, as well as several properties, examples related to the _file list_.

Basically, the _file list_ is the sorted list of valid _relative paths_ of _worth-considering files_ in the _given directory_. For definitions of _relative paths_, _worth-considering files_, please read `File list.md`.

## Definition of a "test case"

- A _test case_ is a pair of two file names:
  + The first item is called the _input file_ of the _test case_.
  + The second item is called the _output file_ of the _test case_.

- A _test case_ is considered to be valid iff
  + _input file_ and _output file_ are different, and
  + _input file_ and _output file_ exist in the _file list_.

## Definition and properties of a "spec"

- A _spec_ is a struct of these three properties:
  + _input spec_: a string
  + _output spec_: a string
  + _spec type_: a char, can only be `^` or `$`

- A _spec_ is considered to be valid iff
  + _input spec_ and _output spec_ do not contain any uppercase letters, and
  + _input spec_ and _output spec_ do not contain any of the following restricted characters `< > : " / \ | ? *` (note that space is not a restricted character).

- We say a valid _spec_ S matches a _test case_ T with type `^` iff
  + _spec type_ of S is `^`, and
  + _input spec_ of S is a prefix of _input file_ of T, and
  + _output spec_ of S is a prefix of _output file_ of T, and
  + `T.inputFile - S.input_spec == T.outputFile - S.output_spec`.
  Note that, in the paragraph above, A-B is the string obtained by removing `length(B)` characters from the beginning of A.

- We say a valid _spec_ S matches a _test case_ T with type `$` iff
  + _spec type_ of S is `$`, and
  + _input spec_ of S is a suffix of _input file_ of T, and
  + _output spec_ of S is a suffix of _output file_ of T, and
  + `T.inputFile - S.input_spec == T.outputFile - S.output_spec`.
  Note that, in the paragraph above, A-B is the string obtained by removing `length(B)` characters from the end of A.

- We say a valid _spec_ S matches a _test case_ T iff
  + S matches T with type `^`, or
  + S matches T with type `$`.

## Definition and properties of a "test list"

- A _test list_ is a list of _test cases_, associated with a _spec_.

- A _test list_ is considered to be valid iff
  + each _test case_ is a valid _test case_, and
  + each file name in the _test list_ appears only once, and
  + each _test case_ matches the _spec_ if the _test list_.

- We say a _spec_ is approved if it is listed in `approved_spec_list.txt`.

- We define _keyword score_ of a _spec_ to be sum of the following values
  + Number of strings listed in `input_keyword_list.txt` which is a substring of _input spec_.
  + Number of strings listed in `output_keyword_list.txt` which is a substring of _input spec_.

- We define _vowel score_ of a _spec_ as follow:
  + Let a1, e1, i1, o1, u1 be number of occurences of 'a', 'e', 'i', 'o', 'u' in _input spec_, respectively, case-insensitively.
  + Let a2, e2, i2, o2, u2 be number of occurences of 'a', 'e', 'i', 'o', 'u' in _output spec_, respectively, case-insensitively.
  + Then, _vowel score_ is defined to be (-a1-e1+i1-o1-u1) + (a2+e2-i2+o2+u2).

- If P and Q are two valid _test lists_, they can be compared as follow:
  + First, compare lengths. The longer the better.
  + Then, check approval. Approved is better than not approved.
  + Then, compare _keyword scores_. The higher the better.
  + Then, compare _vowel scores_. The higher the better.
  + If the rules above cannot decide which is better, we conclude P is as good as Q.

