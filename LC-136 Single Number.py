"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

"""

# O(1) space (constant)
# O(n) time (linear)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]

        for i in range(1, len(nums)):
            # use the XOR operator to cancel out duplicates
            result ^= nums[i]

        return result
