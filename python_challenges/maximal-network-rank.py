from collections import defaultdict
# From leetcode
# NOTE: Different places have slight variations of this question.
# If only the network ranks of adjacent cities matters, a simple, fast solution is available
# If the maximal network rank could be found in cities x, y where x and y are not adjacent, more thought is needed
class Solution:
    # This solution assumes network rank is only considered if the cities are connected
    def maximalNetworkRank_SIMPLE(self, n: int, roads: List[List[int]]) -> int:
        
        # ith value is the number of neighbors of i
        num_neighbors = defaultdict(int)
        # adjacency check
        adj = defaultdict(lambda: False)
        
        max_network_rank = 0
       
        for item in roads:
            num_neighbors[item[0]] += 1
            num_neighbors[item[1]] += 1
        
        # ASSUME the only network ranks we observe are for adjacent cities
        for item in roads:
            max_network_rank = max(max_network_rank, num_neighbors[item[0]] + num_neighbors[item[1]] - 1)
        
        return max_network_rank
    
    # This solution assumes the maximal network rank could be for cities x,y where x and y are not adjacent        
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
      
        # ith value is the number of neighbors of i
        num_neighbors = defaultdict(int)
        # adjacency check
        adj = [[False]*n for i in range(n)]
        
        max_network_rank = 0
        
        # build adjacency dict (Simple counts - not named connections)
        for item in roads:
            x, y = item[0], item[1]
            # both cities get 1 more connection
            num_neighbors[x] += 1
            num_neighbors[y] += 1
            #how to use unordered tuple as key?
            adj[x][y] = True
            adj[y][x] = True
        
        # N^2 runtime. Need faster algorithm.
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                else:
                    # Sum of neighbors of both cities
                    curr_network_rank = num_neighbors[i] + num_neighbors[j]
                    # If they are adjacent you need to discount their connection
                    if adj[i][j] == True:
                        curr_network_rank -= 1
                    max_network_rank = max(max_network_rank, curr_network_rank)
        
        return max_network_rank
