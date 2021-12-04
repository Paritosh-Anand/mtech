#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums=[], target=None):
        
        if len(nums) <= 0 and target is None:
            exit()
        
        seen = {}
        for index, num in enumerate(nums):
            x = target - num
            if x not in seen.keys():
                seen[num] = index
            else:
                # print(f'Found {index} and {seen.get(x)} for target {target}')
                return [seen.get(x), index]

# @lc code=end

