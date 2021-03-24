# From CTCI:
# given string s, b, find all permutations of s in b

# QUICK AND DIRTY but O(n)
print("Hello world")
from collections import defaultdict

s = 'abbc'
s_dict = defaultdict(int)

# Fill out char count for s
for char in s:
    s_dict[char] += 1
# Cheat! Find a way to delete key when it goes to zero
# Or, prepopulate keys with the unique keys of b
s_dict['d'] = 0 
    
b = 'cbabadcbbabbcbabaabccbabc'
print(len(b))
b_dict = defaultdict(int)

# initialize "current substring character count"; leftmost substring of b with length equal to length of s
for i in range(len(s)):
    b_dict[s[i]] += 1
# Cheat!
b_dict['d'] = 0 

permutations = []
for i in range(len(b) - 3):
    substring = b[i:i+4]
    print(substring)
    if b_dict == s_dict:
        # print(substring)
        print(b_dict)
        print(s_dict)
        permutations.append(substring)
    # update curr substr char count; subtract 1st letter, add next letter
    if i == len(b) - 4:
        break
    first_char = b[i]
    next_char  = b[i+4]
    b_dict[first_char]  -= 1
    b_dict[next_char]   += 1
    # print(i, i+3)
    # print(b[i:i+4])
print(permutations)
