# Variation 1 (Easier):
lst1 = [1, 2, 2, 4, 7, 9]
lst2 = [2, 5, 10, 11]

lst1_counter = 0
for item in lst2:
    # If list2 item is <= curr list1 item, insert it before
      while item > lst1[lst1_counter]:
          lst1_counter += 1
          # youve iterated to end of nums1; just put the item there
          if lst1_counter >= len(lst1):
              break
      lst1.insert(lst1_counter, item)
       
print(lst1)

# Variation 2 (Harder):
# Modify Array 1 in place, don't return anything
# Array 1 has trailing zeroes to represent empty slots for numbers from array 2
# m = number of initialized elements in nums1, n = number of initialized elements in nums2
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    # Prune the excess zeroes in nums1
    num_zeroes = len(nums1) - m
    for i in range(num_zeroes):
        del nums1[-1]

    nums1_counter = 0
    for item in nums2:
        while nums1_counter < len(nums1):
            if item <= nums1[nums1_counter]:
                break
            nums1_counter += 1
        nums1.insert(nums1_counter, item)
            
