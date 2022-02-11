"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_chars = {}
        # add all letters from s1 to a hash table
        for char in s1:
            if not s1_chars.get(char):
                s1_chars[char] = 0
            s1_chars[char] += 1

        print('s1_chars', s1_chars)

        start = 0
        end = 0

        s2_chars = {}
        s2_chars[s2[0]] = 1

        # use sliding window on s2 and keep track of all characters in the window
        # by adding them to a hash table
        if s1_chars == s2_chars:
            return True

        while end < len(s2)-1:

            if end - start >= len(s1)-1:

                s2_chars[s2[start]] -= 1

                if s2_chars[s2[start]] == 0:
                    del s2_chars[s2[start]]

                start += 1

            end += 1

            if not s2_chars.get(s2[end]):
                s2_chars[s2[end]] = 0
            s2_chars[s2[end]] += 1

            # if the two hash tables are equal then return true
            if s1_chars == s2_chars:
                return True

        return False
