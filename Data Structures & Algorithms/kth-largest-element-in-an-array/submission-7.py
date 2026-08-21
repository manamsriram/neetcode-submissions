class Solution:
    def findKthLargest(self, nums, k):
        # convert to get the index of kth largest after sorting.
        k = len(nums) - k

        def quickSelect(l, r):
            # pivot can be any random integer, we choose last element
            pivot = nums[r]
            # starts at left most index of current sub array
            # tracks the index to swap in the lesser values
            p = l
            # after the loop, all elements to the left of p are lesser than pivot
            # and p is the index of pivot element if sorted
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return quickSelect(l, p - 1)

        return quickSelect(0, len(nums) - 1)