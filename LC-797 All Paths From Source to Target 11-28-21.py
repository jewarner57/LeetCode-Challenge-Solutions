"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Ex 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""


# Working Solution
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # use backtracking to find all paths
        self.completePaths = []
        self.findPaths(0, graph)
        
        return self.completePaths
        
    
    def findPaths(self, node, graph, path=[]):
        newPath = list(path)
        newPath.append(node)
        
        # base cases:
        # reached the n-1 node
        if node == len(graph)-1:
            self.completePaths.append(newPath)
            return 
        # reached a node with no visitable neighbors
        if len(graph[node]) == 0:
            return
        
        # for each avaliable path from the current node
        for i in range(0, len(graph[node])):
            self.findPaths(graph[node][i], graph, newPath)