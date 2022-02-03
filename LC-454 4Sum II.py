"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples(i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:
Input: nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
"""


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # solution_list = []
        solution_count = 0

        value_combination_dict = {}
        # add up every possible value combination for the first two lists
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                sum = nums1[i] + nums2[j]
                # and add the nums to use sum as the key
                # and the value as the indexes
                if(value_combination_dict.get(sum)):
                    # use an array in case there are multiple with the same sum
                    value_combination_dict[sum].append((i, j))
                else:
                    value_combination_dict[sum] = [(i, j)]

        # add up every possible value combination for the second two lists
        for k in range(0, len(nums3)):
            for l in range(0, len(nums4)):
                sum2 = nums3[k] + nums4[l]

                # if one of those combinations values is in the hash table then
                mirror_combination = value_combination_dict.get(0 - sum2)
                if mirror_combination:
                    solution_count += len(mirror_combination)
                    # for mirror in mirror_combination:
                    #     # add the the hash table indexes plus the current indexes to the solution list
                    #     solution_list.append((mirror[0], mirror[1], k, l))

        # return len(solution_list)
        return solution_count
