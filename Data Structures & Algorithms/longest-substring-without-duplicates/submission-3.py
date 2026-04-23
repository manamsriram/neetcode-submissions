class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        ans=1
        l,h=0,1
        d={s[0]:1}
        longest=1
        while(h<len(s)):
            if(s[h] in d):
                if(longest<(h-l)):
                    longest=h-l
                while(s[h] in d):
                    d.pop(s[l])
                    l+=1
            else:
                d[s[h]]=1
                h+=1
                if(longest<(h-l)):
                    longest=h-l
        return longest