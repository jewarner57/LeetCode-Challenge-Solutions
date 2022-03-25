"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Example 1:
Input: costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Example 2:
Input: costs = [[259, 770], [448, 54], [
    926, 667], [184, 139], [840, 118], [577, 469]]
Output: 1859

Example 3:
Input: costs = [[515, 563], [451, 713], [537, 709], [
    343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]
Output: 3086
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        groupA, groupB = [], []
        
        # go through and add each person to the city that they have the lowest cost to
        for person in costs:
            if person[0] < person[1]:
                groupA.append(person)
                continue
            groupB.append(person)

        # If the arrays are not equal in size
            # sort the larger resulting array by the cost of traveling to the other city
        smallgroup = groupB
        largegroup = groupA
            
        if len(groupA) > len(groupB):
            groupA.sort(key=lambda x : x[0] - x[1])
            
        if len(groupB) > len(groupA):
            largegroup = groupB
            smallgroup = groupA
            
            groupB.sort(key=lambda x : x[1] - x[0])
        

        # remove from the sorted larger list and add to the smaller list until they are equal
        while not len(smallgroup) == len(largegroup):
            smallgroup.append(largegroup.pop())
        

        totalCost = 0
        # return the total cost
        for cost in groupA:
            totalCost += cost[0]
        for cost in groupB:
            totalCost += cost[1]
        
        return totalCost
