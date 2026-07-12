class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def dfs(i, a):
            if len(a) == len(digits):
                res.append(a)
                return
            # this is essentially a nested for loops of size len(digits)
            for char in digitToChar[digits[i]]:
                dfs(i + 1, a + char)
        
        if digits:
            dfs(0, '')
        return res

