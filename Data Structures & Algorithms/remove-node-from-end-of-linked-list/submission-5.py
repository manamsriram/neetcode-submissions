# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = head
        count = 0
        while head:
            count += 1
            head = head.next
        count = count - n
        head = ans.next
        while count > 0:
            if(count == 1 and head.next):
                break
            head = head.next
            count -= 1
        if ans.next == head and count == 0:
            ans.next = ans.next.next
        else:
            head.next = head.next.next
        return ans.next



