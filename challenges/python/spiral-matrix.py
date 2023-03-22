# LC54
# Currently not working with time limit exceeded
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        run = len(matrix)
        rise = len(matrix[0])
        total = run * rise

        visited = set()
        ret = []

        i = 0
        j = 0

        i_direc = 1
        j_direc = 1


        num_visited = 0
        while num_visited < 5:
            while 0 < i < run and (i, j) not in visited:
                visited.add((i, j))
                print(i, j)
                num_visited += 1
                ret.append(matrix[i][j])
                i += i_direc

            i_direc = -i_direc
            i += i_direc
            
            while 0 < j < rise and (i, j) not in visited:
                visited.add((i, j))
                print(i, j)
                num_visited += 1
                ret.append(matrix[i][j])
                j += j_direc

            j_direc = -j_direc
            j += j_direc
            
        return ret

        # 00
        # 01
        # 02
        # 12
        # 22
        # 21
        # 20
        # 10
        # 11
        # DONE

        # 00
        # 01
        # 02
        # 03
        # 13
        # 23
        # 22
        # 21
        # 20
        # 10
        # 11
        # 12

        # Inc 1 axis
        # inc 2nd axis
        # dec 1 axis
        # dec 2 axis
