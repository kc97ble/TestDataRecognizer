# Objective
Given a directory containing test data, output the a valid _test list_, as good as possible.

# Requirements
Let N denote the number of files in the _file list_. The following conditions must be satisfied:
- If N ≤ 128, output must be one of the best _test lists_, i.e. there does not exist any other _test list_ which is better than the output.
- If N > 128, output is generated using a greedy algorithm which will be mentioned later.
- Guarantee of consistency: For each _file list_, the program must output only one output regardless of which OS is used or which computer is used or how many times the program is executed.
- Guarantee of running time: The program must terminate within 1 second on my laptop (Pentium(R) Dual-Core CPU T4400 @ 2.20GHz × 2) for any test cases.

# Assumptions
- Each element in _file list_ must contains only ascii characters from #32 (space character) to #126 (character '~'), except 
- The _file list_ is guaranteed to contain less or equal to 1024 elements.





#Overview of Algorithm
1. List all the files in the given directory.
2. List potential specs.
3. Choose the best spec.
4. If number of tests is larger than 1, go to step 6
5. For each pair of files, choose the best pair
6. Output

#Complexity
- Let N be the number of files
- Let L be the maximum length of a path
- O(N*L)

#Assumptions
- Maximum number of files = 1024
- All files, including hidden files, can be listed successfully
- All testdatas are in either spec XZ|YZ or spec ZX|ZY

#Philosophy
- Maximize number of tests in the output, then maximize the likelihood
- Output must be consistent

#Behaviors
- Max depth = 2
- Hidden files are treated as normal files

