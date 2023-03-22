# LC 14
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_str = ""
        shortest_len = 201
        for item in strs:
            if len(item) < shortest_len:
                shortest_str = item
                shortest_len = len(item)

        print(shortest_str, shortest_len)
        if shortest_len == 0:
            return ""
        i = 0

        while i < shortest_len:
            char = shortest_str[i]
            for item in strs:
                if item[i] != char:
                    return item[:i]

            i += 1

        return shortest_str[:i]
