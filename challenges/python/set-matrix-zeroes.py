# LC73 Set Matrix Zeroes
# Iterate every cell, if zero, add its row and column to a set (hashed)
# Go through list of offending rows and cols and zero the elements
# NOTE: Could save space complexity by using first element of each row and column as an indicator, then put back orig value
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix = 
        #[[0,1,2,0],
        # [3,4,5,2],
        # [1,3,1,5]]
        offending_rows = set()
        offending_cols = set()
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    offending_rows.add(row)
                    offending_cols.add(col)
        
        for i in range(len(matrix)):
            for col in offending_cols:
                matrix[i][col] = 0
                
        for j in range(len(matrix[0])):
            for row in offending_rows:
                matrix[row][j] = 0
