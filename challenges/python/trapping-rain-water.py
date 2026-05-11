# cant just observe adjacent heights...they could be lower than some distant height that
# forms a higher wall, thereby trapping more water
# so do two passes: find highest height to left of every index, and highest to right of every index
# then at each index take min of those to form container and subtract current height to get water
# held at that index
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1 or len(height) == 2:
            return 0
        
        highest_l = {}
        highest_r = {}
        
        curr = 0
        for i in range(len(height)):
            highest_l[i] = curr
            curr = max(curr,height[i])
            
        curr = 0
        for i in range(len(height) - 1, -1, -1):
            highest_r[i] = curr
            curr = max(curr,height[i])
                    
        total = 0
        for i in range(1, len(height)-1):
            curr = min(highest_l[i],highest_r[i]) - height[i]
            curr = max(0, curr)
            total += curr
            
        return total