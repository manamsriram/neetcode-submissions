# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode(0, head)
        l = ans
        r = head

        while n > 0:
            r = r.next
            n -= 1

        while(r): # keep distance between left and right n + 1
            l = l.next
            r = r.next
        # we will have right at the end and left at n+1 distance from the end
        l.next = l.next.next
        return ans.next
