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
        
# should be faster for not reconstructing string repeatedly 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        (shorter, longer) = (word1, word2) if len(word1) < len(word2) else (word2, word1)
        out = []
        i = 0
        print(longer, shorter)
        while i < len(shorter):
            out.append(word1[i])
            out.append(word2[i])
            i += 1
        return ''.join(out) + str(longer[i:])