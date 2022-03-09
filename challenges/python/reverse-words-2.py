# 2nd part of LC challenge
# Modify array of chars in place
# Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output:    ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# My approach: Helper function to reverse characters of string at given start, end
# First, reverse entire string, to put the words in their general place
# Second, loop through, get bounds of words, reverse them in place

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # midpoint arithmetic: (end - start - 1) // 2
        # 0 1 2 3 4   = 2
        # 0 1 2 3 4 5 = 2
        
        def swap_word(s, start, end):
            midpoint = (end - start - 1) // 2
            for i in range(midpoint + 1):
                temp = s[start + i]
                s[start + i] = s[end - i]
                s[end - i] = temp
                
        # First reverse entire word
        swap_word(s, 0, len(s) - 1)
        
        i = 0
        while i < len(s):
            # Find start, end of word
            if s[i] != ' ':
                start = i
                while i < len(s) and s[i] != ' ':
                    i += 1
                end = i
                swap_word(s, start, end - 1)
            i += 1
