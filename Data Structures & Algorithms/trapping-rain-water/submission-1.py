class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        l, r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r :
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]   
        return res


#if leftMax < rightMax:
#min(leftMax, rightMax)
#        ↓
#     leftMax

#min(leftMax, rightMax) = rightMax



#NORMAL FORMULA:

#water = min(maxLeft, maxRight) - height[i]
#              ↑
#        whichever is smaller

#Two pointers:
#if leftMax < rightMax:
#       ↑
# leftMax is smaller

#water = leftMax - height[l]


#else:

#rightMax is smaller

#water = rightMax - height[r]  


#res += leftMax - height[l]
#res += min(leftMax, rightMax) - height[l]
#leftMax < rightMax
