# Given mapping of digits to letters as seen on a telephone,
# Return all possible character combinations that could represent a number
# Explanation:
# We use backtracking
# Dictionary maps each digit to a string of possible chars
# In our main function we have a empty result set, 
# We define a recursive function that has a base case meaning:
# If we have reached the end of the string, its a complete combination, append it to results
# If not: For every letter in dictionary for this digit, we choose that digit to fill this spot
# Then recurse on string from next position
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        d = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        result = []
        
        def recurse(S, i):
            
            if i == len(digits):
                result.append(S)
                return
            
            for letter in d[digits[i]]:
                temp = S + letter
                recurse(temp, i+1)
                
        recurse('', 0)
        return result
