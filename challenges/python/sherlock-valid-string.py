#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-valid-string
# Solved for all cases!

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# aaaaabc
# aaaabbcc
def isValid(s):
    # Write your code here
    found_letters = set()
    letter_frequencies = defaultdict(int)
    
    for letter in s:
        found_letters.add(letter)
        letter_frequencies[letter] += 1
    print("found letters", found_letters)
        
    # num_unique_frequencies = 0
    unique_frequencies = set()
    frequency_counts = defaultdict(int)
    
    for letter in found_letters:
        curr_frequency = letter_frequencies[letter]
        unique_frequencies.add(curr_frequency)
        frequency_counts[curr_frequency] += 1
    
    max_freq = max(unique_frequencies)
    min_freq = min(unique_frequencies)
    spread = abs(min_freq - max_freq)
    
    print("max, min freq", max_freq, min_freq)
    print("unique frequencies", unique_frequencies)
    print("frequency counts", frequency_counts)
    
    # If there is only one unique freq, all letters occur same # of times
    if len(unique_frequencies) == 1:
        return 'YES'
    # If there are more than two unique frequencies string cannot be made valid with one deletion
    elif len(unique_frequencies) > 2:
        return 'NO'
    
    elif len(unique_frequencies) == 2:
        if frequency_counts[max_freq] <= 1 and spread <= 1:
            return 'YES'
        elif frequency_counts[min_freq] <=1 and min_freq == 1:
            return 'YES'
        else:
            return 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
