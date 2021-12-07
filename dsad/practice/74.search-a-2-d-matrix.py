#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        self.m = len(matrix)
        self.n = len(matrix[0])

        # binary search
        left, right = 0, self.m * self.n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // self.n][pivot_idx % self.n]

            if target == pivot_element:
                    return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1

        return False
        
# @lc code=end

matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
target = 30

sol = Solution()
print(sol.searchMatrix(matrix=matrix, target=target))


