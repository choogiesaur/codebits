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

# python gotcha: reconstructing string every time for ans^
class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = []
        vowels = {'a', 'e', 'i', 'o','u',
        'A','E','I','O','U'}
        indices = []
        buttheads = []
        for i, char in enumerate(s):
            if char in vowels:
                arr.append('*')
                indices.append(i)
                buttheads.append(char)
            else:
                arr.append(char)
        
        for idx in indices:
            arr[idx] = buttheads.pop()

        return ''.join(arr)