#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int):
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)] # initialize row elements 
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j] # dynamic programming
            triangle.append(row)
        return triangle
# @lc code=end

sol = Solution()
pascal_triangle = sol.generate(numRows=7)
print(pascal_triangle)
