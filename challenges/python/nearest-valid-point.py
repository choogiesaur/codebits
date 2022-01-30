# Leetcode 1779
# Manhattan distance = |x1 - x2| + |y1 - y2|
# Could simplify for loop declaration with multiple initial values & enumerate() as such:
# for i, (r, c) in enumerate(points):

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index_of_smallest = -1
        smallest_manhattan = 20001
        
        i = 0
        for pair in points:
            # If valid
            if x == pair[0] or y == pair[1]:
                #Calculate manhattan distance
                manhattan = abs(x - pair[0]) + abs(y - pair[1])
                if manhattan < smallest_manhattan:
                    smallest_manhattan = manhattan
                    index_of_smallest = i
            i += 1 
            
        return index_of_smallest
