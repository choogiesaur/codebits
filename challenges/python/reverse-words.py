# LC 151
# Reverse words, removing trailing whitespace
# " the sky is        blue       " ->
# "blue is sky the"
# Multiple spaces between words should be ignored
# words are letters+digits, string can contain spaces

class Solution:
    def reverseWords(self, s: str) -> str:
        parts = [x for x in s.strip().split(' ') if len(x) > 0]
        return ' '.join(parts[::-1])
        
