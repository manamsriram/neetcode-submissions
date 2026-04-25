# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head=ListNode()
        ans=ListNode()
        ans=head
        while(list1 and list2):
            temp=ListNode()
            if(list1.val<=list2.val):
                temp.val=list1.val
                list1=list1.next
            else:
                temp.val=list2.val
                list2=list2.next
            head.next=temp
            head=head.next
        while(list1):
            temp=ListNode()
            temp.val=list1.val
            head.next=temp
            head=head.next
            list1=list1.next
        while(list2):
            temp=ListNode()
            temp.val=list2.val
            head.next=temp
            head=head.next
            list2=list2.next
        return ans.next