# LC 11
# Two pointer approach: 
# Observe current rectangle formed by vertical lines at i and j
# Limiting height is the shorter of the two
# Area is limiting height * width of the rectangle (calculated by j - i)
# Increment inward the pointer corresponding to the shorter side
# This is because selecting a new side to replace the shorter side is the only possible way to increase the contained water
# which would be in the case that the new line used is taller
# (Note that we are pretending any lines that are not the sides or bottom of the container are not there)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1

        max_area = 0
        while i < j:
            width = j - i
            if height[i] < height[j]:
                curr_area = width * height[i]
                i += 1
            else:
                curr_area = width * height[j]
                j -= 1
            max_area = max(max_area, curr_area)
        
        return max_area
