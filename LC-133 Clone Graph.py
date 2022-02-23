"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

https://leetcode.com/problems/clone-graph/
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # for [] case
        if node is None:
            return node
        
        self.visited = {}
        graphCopy = self.copyNode(node)
        return graphCopy
    
    def copyNode(self, node):
        if self.visited.get(node):
            return self.visited[node]
        
        # create a new node
        nodeCopy = Node(node.val)
        
        # save the new node to visited
        self.visited[node] = nodeCopy
        
        # for each of the neighbors
        for neighbor in node.neighbors:
            # check if copy has already been made
            if self.visited.get(neighbor):
                copy = self.visited[neighbor]
                nodeCopy.neighbors.append(copy)
            else:
                # if not then make a copy
                nodeCopy.neighbors.append(self.copyNode(neighbor))
        
        return nodeCopy
