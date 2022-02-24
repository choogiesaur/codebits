# https://www.hackerrank.com/challenges/ctci-making-anagrams
#!/bin/python3

import math
import os
import random
import re
import sys
# added this
from collections import defaultdict

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    adict = defaultdict(int)
    bdict = defaultdict(int)
    
    found_letters = set()
    
    for letter in a:
        adict[letter] += 1
        found_letters.add(letter)
    
    for letter in b:
        bdict[letter] += 1
        found_letters.add(letter)
        
    min_deletions = 0
    for letter in found_letters:
        curr = abs(adict[letter] - bdict[letter])
        min_deletions += curr
        
    return min_deletions
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
