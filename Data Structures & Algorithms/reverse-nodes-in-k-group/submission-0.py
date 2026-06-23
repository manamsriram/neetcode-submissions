# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0 ,head) # this will always point to the beginning

        groupprev = dummy
        while True:
            kth = self.getkth(groupprev, k)
            # if the window size is less than k
            if not kth: 
                break
            
            groupnext = kth.next # marks the beginning of the next group
            prev, cur = groupnext, groupprev.next # prev points to groupnext as the cur should point to prev and when we reverse, it should ultimately happen
            
            while cur != groupnext: 
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
    
            temp = groupprev.next # It was previously poitning to the beginning of the un-reversed window, which is the end of the reversed window
            groupprev.next = kth # link previous group to the new beginning of current group
            groupprev = temp # marks the end of the new previous group
        return dummy.next

    # helper to get the current pointer to the edge of the current k-sized window
    def getkth(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1
        return cur