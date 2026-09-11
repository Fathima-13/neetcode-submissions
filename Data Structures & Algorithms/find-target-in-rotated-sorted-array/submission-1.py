class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r :
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            #left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums [r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1



"""
                 Find mid
                    ↓
            Is nums[mid] target?
               /          \
             YES           NO
              ↓             ↓
           return mid    Which half is sorted?
                         /             \
                    LEFT sorted     RIGHT sorted
                       ↓                 ↓
                 Is target in       Is target in
                 left range?       right range?
                  /     \            /      \
                YES     NO          YES      NO
                 ↓       ↓           ↓        ↓
             r=mid-1  l=mid+1    l=mid+1   r=mid-1
 """
