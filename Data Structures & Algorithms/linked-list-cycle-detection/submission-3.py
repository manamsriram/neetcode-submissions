# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False
        dummy=ListNode()
        dummy.next=head
        slow=head
        fast=head.next.next
        while(slow!=fast):
            if(slow.next==None or fast==None or fast.next==None):
                return False
            slow=slow.next
            fast=fast.next.next
        return True
