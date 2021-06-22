# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.visited = {}

    def clone_graph_recursive(self, node):
        if node is None:
            return node
        
        if node in self.visited:
            return self.visited[node]
    

        new_node = UndirectedGraphNode(node.label)
        self.visited[node] = new_node

        for n in node.neighbours:
            new_node.neighbors.append(self.clone_graph_recursive(n))
        
        return new_node
        
    def cloneGraph(self, node):
        return self.clone_graph_recursive(node)

