# Working solution and the one described many places:
# Decision tree of what you can add to the string at any given moment:
# If you have remaining lefts, you can always add a left (opening) parenthesis
# If so, recurse with added left, and subtract count of remaining lefts (remember to undo action right after calling - principle of backtracking)
# If no remaining lefts, and lefts_remaining less than rights_remaining (You've opened more than youve closed):
# Then you can add a right (closing) parenthesis. Recurse with new str and less remaining rights
# if the current string is equal to double of n, then youve constructed a complete string

# Old attempt:
# gets most possibilities, but unable to construct something like:
# (())(())
# After forming the first half: (())
# And even adding another pair: (())()
# It has no way to generate parentheses in or around the recently added pair to attain (())(())
class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = set()
        
        def recurse(lst, left_remaining, right_remaining):
            if len(lst) == n * 2:
                # Then you've constructed a complete string
                paren_string = "".join(lst)
                if paren_string not in result:
                    result.add(paren_string)
            if left_remaining > 0:
                lst.append('(')
                recurse(lst, left_remaining - 1, right_remaining)
                lst.pop()
            if left_remaining < right_remaining:
                lst.append(')')
                recurse(lst, left_remaining, right_remaining - 1)
                lst.pop()
        
        recurse([], n, n)
        return list(result)
    
    def generateParenthesis_old(self, n: int) -> List[str]:
        
        result = set()
        
        def recurse(n, curr):
            if n == 0:
                if curr not in result:
                    result.add(curr)
            else:
                # option_1 = '(' + curr + ')'
                # option_2 = '()' + curr
                # option_3 = curr + '()'
                recurse(n-1, '(' + curr + ')' )
                recurse(n-1, '()' + curr )
                recurse(n-1, curr + '()' )
                
        
        recurse(n, '')
        return list(result)
