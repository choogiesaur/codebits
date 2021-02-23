# Iterate over lines of two files at once and concatenate individual lines
# Example:
# file 1:   file 2:
# a         lol
# b         blah
# c         mango
# outfile:
# a lol
# b blah
# c mango

file_1 = 'file1.txt'
file_2 = 'file2.txt'

with open(file_1) as bf1, open(file_2) as bf2:
    for line1, line2 in zip(bf1, bf2):
        print(line1.strip() + ' ' + line2.strip())
