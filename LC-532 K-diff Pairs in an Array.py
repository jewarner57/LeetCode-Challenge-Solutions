"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Example 1:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

"""

# O(n) time complexity
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        # put all list items into a hash table
        for i in range(0, len(nums)):
            if not nums_dict.get(nums[i]):
                nums_dict[nums[i]] = []
            nums_dict[nums[i]].append(i)

        result_dict = {}

        # for each item check if its k sum counterparts exist
        for i in range(0, len(nums)):
            pair_sum = (nums[i] - k, nums[i] + k)
            pair_list = []

            for pair in pair_sum:
                if nums_dict.get(pair) and (not i == nums_dict.get(pair)[0]):
                    pair_list.append(pair)
                    result_dict[tuple(sorted([nums[i], pair]))] = True

        return (len(result_dict.keys()))
