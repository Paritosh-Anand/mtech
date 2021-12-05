#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        curr_shape_r = len(mat)
        curr_shape_c = len(mat[0])

        if (curr_shape_r * curr_shape_c) == (r * c):
            # print("reshape is possible")
            ans = [[]]
            for rows in mat:
                for item in rows:
                    if(len(ans[-1]) < c): # there are empty columns in the last row of ans matrix
                        ans[-1].append(item)
                    else:
                        ans.append([])
                        ans[-1].append(item)
            return ans
        else:
            # print("reshape is NOT possible")
            return mat
        
# @lc code=end


sol = Solution()
ans = sol.matrixReshape([[1,2,5],[3,4,6]], r = 3, c = 2)
print(ans)
