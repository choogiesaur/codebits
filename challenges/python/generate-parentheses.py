# First attempt:
# gets most possibilities, but unable to construct something like:
# (())(())
# After forming the first half: (())
# And even adding another pair: (())()
# It has no way to generate parentheses in or around the recently added pair to attain (())(())
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
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
