# LC 151
# Reverse words, removing trailing whitespace
# " the sky is        blue       " ->
# "blue is sky the"
# Multiple spaces between words should be ignored
# words are letters+digits, string can contain spaces

class Solution:
    # Practice this one again, because I kept forgetting function usages
    # Key points: python .isalnum(), reversed() takes in list as arg in parentheses, strip() to remove whitespace
    def reverseWordsPythonic(self, s: str) -> str:
        parts = s.split(" ")

        ordered = [word.strip() for word in reversed(parts) if word.strip().isalnum() ]

        return ' '.join(ordered)
        
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        reversed_tokens = []
        
        curr_word = ''
        i = 0
        while i < len(s):
            # start forming current word
            if s[i] != ' ':
                curr_word += s[i]
            # if space encountered, record word in list and reset to empty string, then advance past all spaces
            elif s[i] == ' ':
                reversed_tokens = [ curr_word ] + reversed_tokens
                curr_word = ''
                while s[i] == ' ':
                    i += 1
                continue
            i += 1
        
        if curr_word != '':
            reversed_tokens = [ curr_word ] + reversed_tokens
        
        return ' '.join(reversed_tokens)
