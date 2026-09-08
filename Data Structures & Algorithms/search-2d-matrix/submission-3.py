class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break  # So this is the correct row where the target could exist.
        
        if not (top <= bot):
            return False # If we searched all possible rows and couldn't find a row where the target could belong:
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


"""
ROWS, COLS = len(matrix), len(matrix[0])
len(matrix) = 3 

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

Python sees this as one list containing 3 other lists


len(matrix[0]) = 4
        matrix[0] means the first row:
    len(matrix[0]) How many elements are in the first row?




----
        if not (top <= bot):
            return False

matrix = [
    [1, 3, 5],
    [10, 12, 15],
    [20, 25, 30]
]

target = 17
bigger than 15
smaller than 20

There is no possible row containing 17.
top > bot
return False
"""