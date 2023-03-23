# LC 54 Spiral Matrix (Medium)
# Return spiral order traversal of matrix
# This solution involves incrementing i, j and flipping the direction when you hit an edge (visited node)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        total_cells = m * n

        visited = set()
        ret = []

        (i, j) = (0, 0)

        i_direc = 1
        j_direc = 1

        count = 0
        while count < total_cells:
            while -1 < j < n:
                if (i, j) not in visited:
                    visited.add((i,j))
                    print("visited ", i, j, matrix[i][j])
                    count += 1
                    ret.append(matrix[i][j])
                else:
                    break
                j += j_direc
            
            # Flip direction of j incrementation
            j_direc = -j_direc
            j += j_direc
            i += i_direc

            while -1 < i < m:
                if (i, j) not in visited:
                    visited.add((i, j))
                    print("visited ", i, j, matrix[i][j])
                    count += 1
                    ret.append(matrix[i][j])
                else:
                    break
                i += i_direc

            # Flip j
            i_direc = -i_direc
            i += i_direc
            j += j_direc
        
        return ret
