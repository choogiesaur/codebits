# https://www.hackerrank.com/challenges/frequency-queries/

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Works for most test cases.
# Operation 3 is slow; solution could be some sort of reverse lookup dictionary where:
# key is frequency, value is True/False if an item of that frequency exists
# At the moment any time there is a 3 operation it iterates through all dictionary items
# Complete the freqQuery function below.
def freqQuery(queries):
    occurrences = defaultdict(int)
    freq_exists = defaultdict(int)
    results = []
    
    for query in queries:
        oper = query[0]
        data = query[1]
        
        if oper == 1:
            occurrences[data] += 1
        
        if oper == 2:
            if occurrences[data] > 1:
                occurrences[data] -= 1
        
        if oper == 3:
            found = False
            for k, v in occurrences.items():
                if v == data:
                    found = True
                    break
            if found == True:
                results.append(1)
                print(1)
            else:
                results.append(0)
                print(0)
           
    return results
            
