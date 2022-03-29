"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use hash table
        foundNums = {}
        for num in nums:
            if foundNums.get(num):
                return num
            foundNums[num] = True
            
        return -1    
        
        