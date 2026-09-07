class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1













               # while l <= r:  # <= cause it shows if the left point has crossed the right or not
                        # let say this is our array [1] both left and right are 
                        # pointing to the  same  place our mid pointer as well
                        # and out target = 2 
           # l = m + 1   # l = 1 left pointer will be 1 pointer and right pointer as r = 0 that's how we know we have no more values left