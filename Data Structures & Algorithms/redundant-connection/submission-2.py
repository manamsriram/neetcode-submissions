class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # number of nodes as one edge is added we have n edges and n nodes
        n = len(edges)
        # tracks root parent up a chain of connections and stores only root, handled by find
        # every node is it's own parent in the beginning 
        parent = [i for i in range(n + 1)]
        # stores the size of the tree from this root
        # we only ever care about the root's size, as it is aprent to all nodes
        rank = [1 for i in range(n + 1)]

        # finds the parent node and traces it back to the root through it's connecting edges
        # root is the node where it's parent is itself
        def find(n):
            par = parent[n]
            while par != parent[par]:
                # we link current node to it's granparent and switch there
                parent[par] = parent[parent[par]]
                par = parent[par]
            return par

        # add edge and combine them or return False, if it is already in the tree
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # this means they have the same root parent and have gone been unioned
            if p1 == p2:
                return False

            # connect the tree with less nodes to the tree with more nodes, so higher rank tree is common root and we ignore the lower rank
            if rank[p2] < rank[p1]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []