"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into 
on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""


# Solution
from functools import lru_cache

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.cache = {}
        
        if len(nums) <= 2:
            return max(nums)
        
        return self.visit_house(0, 0)
        
    @lru_cache(maxsize=None)
    def visit_house(self, location, total):
        # we are at the last house or second to last house
        if location > len(self.nums)-1:
            return total
        
        # rob the current house
        rob_dis = self.visit_house(location+2, total+self.nums[location])
        # do not rob the current house
        no_rob = self.visit_house(location+1, total)
        
        return max(rob_dis, no_rob)