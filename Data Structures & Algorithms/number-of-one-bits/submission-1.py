class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Subtracting 1 from a number flips the rightmost 1 bit to 0 and turns all bits to its right into 1
            # Performing n & (n - 1) removes the rightmost 1 bit from n
            n = n & n - 1
            count += 1
        return count