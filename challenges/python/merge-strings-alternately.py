# LC 1768 - Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        j = 0

        out = ""

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                out = out + word1[i]
                i += 1
            if j < len(word2):
                out = out + word2[j]
                j += 1
        
        return out
