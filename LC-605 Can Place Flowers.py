"""
You have a long flowerbed in which some of the plots are planted, and some
are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return if n new flowers can be
planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true


Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        newFlowers = 0
        newbed = flowerbed

        # Loop through and add flowers
        for i in range(0, len(newbed)):
            leftVal = 0
            rightVal = 0

            # prevent out of bounds errors
            if not i-1 < 0:
                leftVal = newbed[i-1]

            if not i+1 > len(newbed)-1:
                rightVal = newbed[i+1]

            # add anywhere that is possible
            if leftVal == 0 and rightVal == 0 and newbed[i] == 0:
                newbed[i] = 1
                newFlowers += 1

        # return added flowers >= n
        return n <= newFlowers
