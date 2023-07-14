# LC 345
class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = []
        key = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
        for i in range(len(s)):
            if s[i] in key:
                vowels.append(s[i])
        
        ans = ''
        for i in range(len(s)):
            if s[i] in key:
                ans = ans + vowels.pop(-1)
            else:
                ans = ans + s[i]

        return ans
