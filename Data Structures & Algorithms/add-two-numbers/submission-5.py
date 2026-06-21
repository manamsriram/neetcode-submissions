# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur1 = l1
        cur2 = l2

        while cur1 and cur2:
            sum = cur1.val + cur2.val + carry
            carry = 0
            if sum > 9:
                carry = 1
                sum %= 10
            cur1.val = sum
            
            if cur1.next and not cur2.next: # number l1 has more digits
                cur2.next = ListNode(0) # just add zero as the trailing digit
            elif not cur1.next and cur2.next: # number l2 has more digits
                cur1.next = ListNode(0)
            elif not cur1.next and not cur2.next: # no more digits in both numbers
                if carry:
                    cur1.next = ListNode(carry)
            cur1 = cur1.next
            cur2 = cur2.next
        return l1