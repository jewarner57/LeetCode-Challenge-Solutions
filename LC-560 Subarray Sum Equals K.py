"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1, 1, 1], k = 2
Output: 2

Example 2:
Input: nums = [1, 2, 3], k = 3
Output: 2
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # loop through
        sum = 0
        hashed_sums = {}
        count = 0
        for num in nums:
            # keep sum of current elements of array
            sum += num

            # if current sum equals k add to count
            if sum == k:
                count += 1

            # if sum - k is in hash table then increase count
            if sum-k in hashed_sums:
                count += hashed_sums[sum-k]

             # add current sum to hash table
            if not sum in hashed_sums:
                hashed_sums[sum] = 0
            hashed_sums[sum] += 1

        return count
