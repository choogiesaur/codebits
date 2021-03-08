# Problem: You have a staircase of n steps. You can either take 1 step, or 2 steps at a time.
# Count the number of ways (sequences of step sizes) to get to the top of the staircase.
class Solution:
    
    # Memoization: Initialize with base cases
    global_dic = {
        0:0,
        1:1,
        2:2
    }
    
    def climbStairs(self, n: int) -> int:
        
        # First thing: Check if answer is memo'd
        if n in self.global_dic:
            return self.global_dic[n]
        else:
            # Number of steps to get to one step previous +
            # Number of steps to get to two steps previous
            val = self.climbStairs(n-1) + self.climbStairs(n-2)
            
            # Memo it then return
            self.global_dic[n] = val
            return val
          
        # n = 2
        # 1 1
        # 2 .
        
        # n = 3
        # 1 1 1
        # 2 . 1
        
        # n = 4
        # 1 1 1 1
        # 2 . 1 1
        # 1 2 . 1
        # 1 1 2 .  
        # 2 . 2 .
