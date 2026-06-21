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
        if not head:
            return head

        dummy = Node(0, head, None)
        newHead = Node(head.val, None, None)
        dummy2 = Node(0, newHead, None)
        head = head.next

        while head:
            temp = Node(head.val, None, None)
            newHead.next = temp
            newHead = newHead.next
            head = head.next
        head = dummy.next
        newHead = dummy2.next

        d1={}
        d2={}
        i = 0
        while(head):
            d1[head] = i
            head = head.next
            i += 1
        
        head = dummy.next
        i = 0
        while(newHead):
            d2[i] = newHead
            newHead = newHead.next
            i += 1

        newHead = dummy2.next

        i = 0
        while head:
            if head.random:
                newHead.random = d2[d1[head.random]]
            head = head.next
            newHead = newHead.next
            i += 1
        return dummy2.next        