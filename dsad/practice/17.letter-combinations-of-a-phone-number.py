#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0: 
            return []

        self.letters = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }


        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                # print(path, digits)
                combinations.append("".join(path))
                # print(f"combination -- {combinations}")
                return # Backtrack
            
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = self.letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations


        
# @lc code=end

