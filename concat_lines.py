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

with open('file1.txt') as bf1:
    with open('file2.txt') as bf2:
        for line1, line2 in zip(bf1, bf2):
            print(line1.strip() + ' ' + line2.strip())
