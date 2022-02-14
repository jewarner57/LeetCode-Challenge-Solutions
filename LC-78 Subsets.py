"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.find_subset(tuple(nums))

    def find_subset(self, nums):
        if len(nums) == 0:
            return [[]]

        subsets = [nums]
        temp_nums = list(nums)
        for i in range(len(nums)):
            temp_nums.pop(i)

            for subset in self.find_subset(temp_nums):
                if not subset in subsets:
                    subsets.append(subset)

            temp_nums = list(nums)

        return subsets
