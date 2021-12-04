class Solution:
    def containsDuplicate(self, nums) -> bool:
        unique_elements = set()
        for i in nums:
            if i in unique_elements:
                return True
            else:
                unique_elements.add(i)
            
        return False

# l = [1,1,1,3,3,4,3,2,4,2]
# l = [1,2,3,4]

sol = Solution()
print(sol.containsDuplicate(l))