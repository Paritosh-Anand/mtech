#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        sol = []
        i = j = 0
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i] < nums2[j]):
                i += 1
            elif(nums1[i] > nums2[j]):
                j += 1
            else:
                sol.append(nums1[i])
                i += 1
                j += 1
        
        return sol

            
        
# @lc code=end

