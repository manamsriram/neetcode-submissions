class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # flyods algorithm
        # since the nummbers are in range of 1 to n, every value at an index will also be pointing to a value at nums[value]
        slow, fast = 0, 0
        while True: # go until slow and fast pointers meet in the cycle of the linked list
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        p = 0 # intuition is that the distance between the start of the list to start of the cyle is the same as the distance between the start of the cycle to the intersection point in cycle
        while p != slow:
            p = nums[p]
            slow = nums[slow]
        return p