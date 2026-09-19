class Solution:
    def reverse(self, x: int) -> int:
        MIN = -1 << 31
        MAX = (1 << 31) - 1

        sign = -1 if x < 0 else 1
        if sign == -1:
            x = abs(x)

        ans = 0
        while x:
            # % returns different values for negatives, so we have to make the number positive before computing %
            digit = x % 10
            # int(/) rounds towards 0 and // rounds towards negative inf for negatives
            # so -123 // 10 becomes -13 and not -12 like we want here 
            x = int(x / 10)

            if ans > MAX // 10 or (ans == MAX // 10 and digit > MAX % 10):
                return 0
            
            # if ans < MIN // 10 or (ans == MIN // 10 and digit < MIN % 10):
            #     return 0

            ans = ans * 10 + digit

        return ans if sign == 1 else -1 * ans