class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p, s] for p, s in zip(position, speed)] #list comprehension

        stack = [] #We are storing the time each car takes to reach the target.

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s) #time = distance / speed
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    

#target = 12
#p = 10
#s = 2

#Distance:
#12 - 10 = 2

#Time:
#2 / 2 = 1 hour
