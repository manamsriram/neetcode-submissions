class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for c in s:
            if(c.isalnum()):
                st+=c.lower()
        return st==st[::-1]