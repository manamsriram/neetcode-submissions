class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        dict1={}
        dict2={}
        for i in range(len(s)):
            if(s[i] in dict1):
                dict1[s[i]]+=1
            else:
                dict1[s[i]]=1
            if(t[i] in dict2):
                dict2[t[i]]+=1
            else:
                dict2[t[i]]=1
        for i in dict1:
            if(i in dict2):
                if (dict1[i]!=dict2[i]):
                    return False
            else:
                return False
        return True