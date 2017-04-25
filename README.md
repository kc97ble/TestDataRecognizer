# Objective
Given a directory containing test files, output the a valid _test list_, as good as possible.




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

