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


    #2nd solution 2025
    #previous one was better ;)
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        cleanup_list = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cleanup_list.append((i,j))
            
        for item in cleanup_list:
            x = item[0]
            y = item[1]
            
            # lock y and 0 everything in this col
            for i in range(m):
                matrix[i][y] = 0
                
            # lock x and 0 everything in this row
            for i in range(n):
                matrix[x][i] = 0
                
            # IMPROVEMENT:
            # if something is in the cleanup list, dont add any more pairs in its row or column
            # as that row and column is already gonna get processed
