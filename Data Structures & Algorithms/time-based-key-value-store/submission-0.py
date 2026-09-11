class TimeMap:

    def __init__(self):
        self.store = {} #key : list of [ val, timestamp]


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
"""
#values = self.store.get(key, [])
#self.store = {
#    "foo": [
#        ["bar", 1],
#        ["bar2", 4],
#        ["bar3", 7]
#    ]
#}

#values = self.store.get("foo", [])
#[
#    ["bar", 1],
#    ["bar2", 4],
#    ["bar3", 7]
#]

values = [
    ["bar", 1],
    ["bar2", 4],
    ["bar3", 7],
    ["bar4", 10]
]

timestamp = 6

l = 2
r = 3

m = (2 + 3) // 2
m = 2
values[2] = ["bar3", 7]

7 <= 6 ❌

So we go into else:
r = m - 1  r = 2 - 1
r = 1

l = 2
r = 1
while l <= r:
2 <= 1 ❌
So the while loop ends.

"""





