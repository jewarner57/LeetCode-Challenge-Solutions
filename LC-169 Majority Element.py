"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        char_count = {}
        majority_count = 0
        majority_elem = -1
        for num in nums:
            if char_count.get(num) == None:
                char_count[num] = 0
            char_count[num] += 1

            if char_count[num] > majority_count:
                majority_count = char_count[num]
                majority_elem = num

        return majority_elem
