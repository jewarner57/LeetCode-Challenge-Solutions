"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.


Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167


Example 2:

Input: nums = [1,5]
Output: 10
 
"""

# Program does not complete tests within time limit
# but it achieves correct responses and
# sucessfully implements backtracking with memoization
# so Im keeping it anyway


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.store = {}
        return self.popBalloons(nums)

    def popBalloons(self, nums):
        # base case: no more balloons to pop
        if len(nums) == 0:
            return 0

        # check if params exist in store
        callKey = '-'.join(str(n) for n in nums)
        if self.store.get(callKey) is not None:
            # use the store value
            return self.store.get(callKey)

        # for every balloon
        # get the highest coin value
        highestCoins = 0
        for i in range(0, len(nums)):

            # get left and right values
            left = 1
            if i-1 in range(0, len(nums)):
                left = nums[i-1]
            right = 1
            if i+1 in range(0, len(nums)):
                right = nums[i+1]

            # get the coin val
            newCoins = left * right * nums[i]

            # create a new deep copy of balloon arr
            # using slice notation
            newArr = nums[:]
            # pop balloon
            newArr.pop(i)

            # is the call already in the store?
            popKey = '-'.join(str(n) for n in newArr)
            if self.store.get(popKey) is not None:
                # use the store value
                popRes = self.store.get(popKey)
            else:
                # recursive call
                popRes = self.popBalloons(newArr)

            popRes += newCoins

            if popRes > highestCoins:
                highestCoins = popRes

        self.store['-'.join(str(n) for n in nums)] = highestCoins
        return highestCoins
