class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        sol = 0
        mp = {}
        
        i = 0
        
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
                
            sol = max(sol, j - i + 1)
            mp[s[j]] = j + 1
            
        return sol
                