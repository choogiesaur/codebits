class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output an array where arr[x] is product of all items left of x
        prev = 1
        left_product = []
        for num in nums:
            left_product.append(prev)
            prev *= num
        
        # do same for products to the right
        prev = 1
        rite_product = []
        for num in reversed(nums):
            rite_product.append(prev)
            prev *= num

        # now for each element, we have the products of everything to the left
        # and everything to the right
        # so we can multiply these to get our output
      
        out = []
        i = 0
        for item in reversed(rite_product):
            out.append(left_product[i]*item)
            i += 1

        return out
