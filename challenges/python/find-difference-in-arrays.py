# LC 2215
# Return list of lists, first element is list of all elems of 1 not in 2, second is all 2's not in 1
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1 = set(nums1)
        set2 = set(nums2)

        lst1 = []
        lst2 = []

        for item in set1:
            if item not in set2:
                lst1.append(item)
        
        for item in set2:
            if item not in set1:
                lst2.append(item)

        return [lst1, lst2]
