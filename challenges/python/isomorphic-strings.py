# LC 205
# Another solution I wrote that was slightly faster; Array of encodings instead of incremented char
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # traverse strings and encode to number

        s_dict = {}
        curr = 0
        s_rep = []
        for char in s:
            # Either pick an encoding for curr char
            if char not in s_dict:
                s_dict[char] = curr
                s_rep.append(curr)
                curr += 1
            # or retrieve its encoding from dict
            else:
                s_rep.append(s_dict[char])
        
        t_dict = {}
        curr = 0
        t_rep = []
        for char in t:
            if char not in t_dict:
                t_dict[char] = curr
                t_rep.append(curr)
                curr += 1
            else:
                t_rep.append(t_dict[char])
        
        for i in range(len(s_rep)):
            if s_rep[i] != t_rep[i]:
                return False
        
        return True

# Leetcode 205 
# Convert strings to generic representation, which essentially shows how many different characters were used
# if both strings end up with same representation, they are isomorphic
# the representation is kind of like a regex which would match on both
# tough python part here: if the 'inc' value was an int, it would eventually get to double digits and produce two characters for one
# to solve it:
# instead of inc += 1, do
# inc = chr(ord(inc) + 1)
# this is just a way to increment a char in Python ^

from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_dict = {}
        inc = 'a'
        s_rep = ''
        for char in s:
            if char in s_dict:
                s_rep = s_rep + str(s_dict[char])
            else:
                s_dict[char] = inc
                s_rep = s_rep + str(inc)
                inc = chr(ord(inc) + 1)

        t_dict = {}
        inc = 'a'
        t_rep = ''
        for char in t:
            if char in t_dict:
                t_rep = t_rep + str(t_dict[char])
            else:
                t_dict[char] = inc
                t_rep = t_rep + str(inc)
                inc = chr(ord(inc) + 1)

        print(s_rep, t_rep)
        if s_rep == t_rep:
            return True

        return False
