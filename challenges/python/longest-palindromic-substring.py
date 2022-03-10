# Iterates through list, observing longest palindrome radiating from index i
# Even length like abba handled differently from odd length like aba as mid point is between indices for even
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_palindrome = ''
        
        # Odd length palindromes
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindrome_len = r - l + 1
                if palindrome_len > max_len:
                    max_len = palindrome_len
                    max_palindrome = s[l:r+1]
                l -= 1
                r += 1
        
        # Even length palindromes
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindrome_len = r - l + 1
                if palindrome_len > max_len:
                    max_len = palindrome_len
                    max_palindrome = s[l:r+1]
                l -= 1
                r += 1
        
        return max_palindrome
