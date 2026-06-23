# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # we push each linked list wrapped as a NodeWrapper object
        minheap = []
        for i in lists:
            if i is not None:
                heapq.heappush(minheap, NodeWrapper(i))
        # so min heap sorts according to the '<' operator's behaviour
        # which is defined by the NodeWrapper object's __lt__ (dunder method)
        # so, every the root always has the linkedlist with the smallest head element among all lists
        dummy = cur = ListNode(0)
        while minheap:
            node_wrapper = heapq.heappop(minheap)
            cur.next = node_wrapper.node
            if node_wrapper.node.next:
                heapq.heappush(minheap, NodeWrapper(node_wrapper.node.next))
            cur = cur.next
            # we pop the smallest head and then push the rest as another NodeWrapper object
        return dummy.next
        