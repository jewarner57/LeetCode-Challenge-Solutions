"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.candidates = candidates
        self.combos = []

        self.find_unique_combinations([])

        return self.combos

    def find_unique_combinations(self, curr_combo):
        # stop when curr_combo is greater than the target
        if sum(curr_combo) > self.target:
            return

        if sum(curr_combo) == self.target:
            # Sort to prevent different order duplicates
            sorted_combo = sorted(curr_combo)
            # Check if combo already exists
            if sorted_combo not in self.combos:
                self.combos.append(sorted_combo)
            return

        # add a number from candidates to curr_combo each iteration
        for num in self.candidates:
            new_combo = list(curr_combo)
            new_combo.append(num)

            self.find_unique_combinations(new_combo)

        return


# ----------------
# MEMOIZED VERSION
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.candidates = candidates
        self.combos = []

        self.cache = {}

        self.find_unique_combinations(())

        return self.combos

    def find_unique_combinations(self, curr_combo):
        curr_combo = list(curr_combo)

        # stop when curr_combo is greater than the target
        if sum(curr_combo) > self.target:
            return

        if sum(curr_combo) == self.target:
            # Sort to prevent different order duplicates
            sorted_combo = sorted(curr_combo)
            # Check if combo already exists
            if sorted_combo not in self.combos:
                self.combos.append(sorted_combo)
            return

        # add a number from candidates to curr_combo each iteration
        for num in self.candidates:
            new_combo = list(curr_combo)
            new_combo.append(num)
            new_combo = tuple(sorted(new_combo))

            if(not self.cache.get(new_combo)):
                self.cache[new_combo] = True
                self.find_unique_combinations(new_combo)

        return
