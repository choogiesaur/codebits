from collections import defaultdict
# From leetcode
class Solution:
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
