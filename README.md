# Objective
Input: a path of a directory containing test data
Output: a valid _test list_, as good as possible, satisfying the requirements below

# Requirements
Let N denote the number of files in the _file list_. The following conditions must be satisfied:
- If N ≤ 128, output must be one of the best _test lists_, i.e. there does not exist any other _test list_ which is better than the output.
- If N > 128, output is generated using a greedy algorithm which will be mentioned later.
- Guarantee of consistency: For each _file list_, the program must output only one output regardless of which OS is used or which computer is used or how many times the program is executed.
- Guarantee of running time: The program must terminate within 1 second on my laptop (Pentium(R) Dual-Core CPU T4400 @ 2.20GHz × 2) for any test cases.

# Algorithm for N ≤ 128

- Let L be a list of _spec_. Initially, L is empty.
- For each approved _spec_, add it into L.
- For each pair of _relative paths_ in the _file list_, add its _suffix spec_ into L.
- For each pair of _relative paths_ in the _file list_, add its _prefix spec_ into L.
- Let S be the best _spec_ in L.
- Output the maximum _test list_ of S.

