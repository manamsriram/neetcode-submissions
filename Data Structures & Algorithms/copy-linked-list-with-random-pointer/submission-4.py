"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # One pass hash map

        if not head:
            return head

        # link old nodes to the new one, without any connections between them
        d = collections.defaultdict(lambda: Node(0)) # creates an empty if we try to access values not present in dictionary
        d[None] = None # edge case where we reach the end node

        cur = head
        while cur:
            d[cur].val = cur.val
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]