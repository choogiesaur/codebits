# sorting word:
# join sorted(str) on ''
# you get a str with the characters sorted
# all anagrams will share this "signature"
# its hashable so you can use that as key for a dict
# each key will be to a bucket, when we find a new anagram we append it to that bucket
# by accessing with the key and appending to the list we created to start
# then at the end we have a list comp to output the values from our buckets, each is already an array so we make an array of those arrays
# tip: sorted array, think of using two pointer approach
# unsorted, think of using hashmaps
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}

        for str in strs:
            sword = ''.join(sorted(str))

            if sword not in buckets:
                buckets[sword] = []
            buckets[sword].append(str)

        return [buckets[x] for x in buckets.keys()]
