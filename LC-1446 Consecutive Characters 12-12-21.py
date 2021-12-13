"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.
Given a string s, return the power of s.

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
"""

class Solution:
    def maxPower(self, s: str) -> int:
        # O(n)
        # loop through
        largestStreak = -1
        currStreak = 0
        prev = ""
        for letter in s:
            # keep track of longest single character sequence
            if letter == prev:
                currStreak += 1
            else:
                currStreak = 1
            
            if largestStreak < currStreak:
                largestStreak = currStreak
            
            prev = letter
            
        # return the longest sequence
        return largestStreak