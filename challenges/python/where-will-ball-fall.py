#LC 1706
# Passes about half the cases. 
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        ret = []

        num_balls = (len(grid[0]))
        num_rows = len(grid)

        for ball in range(num_balls):
            i = 0
            j = ball

            while True:
                # Direct right
                if grid[i][j] == 1:
                    if j + 1 >= num_balls or grid[i][j+1] == -1:
                        ret.append(-1)
                        break
                    else:
                        i += 1
                        j += 1
                # Direct left
                elif grid[i][j] == -1:
                    if i == 0 or grid[i][j-1] == 1:
                        ret.append(-1)
                        break
                    else:
                        i += 1
                        j -= 1

                # Final check if you've advanced past bottom of grid
                if i == num_rows:
                    ret.append(j)
                    break

        return ret
