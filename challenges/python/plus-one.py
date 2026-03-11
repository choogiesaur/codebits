class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #      0   1   2
        #     -3  -2  -1
        #     [9] [9] [9] ->
        # [1] [0] [0] [0]
        
        ptr = 1
        while ptr <= len(digits):
            if digits[-ptr] < 9:
                digits[-ptr] += 1
                return digits
            digits[-ptr] = 0
            ptr += 1
            
        return [1] + digits