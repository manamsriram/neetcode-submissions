class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        ans=[]
        ind=0
        for i in range(len(strs)):
            t=''.join(sorted(strs[i]))
            if(t in d):
                ans[d[t]].append(strs[i])
            else:
                d[t]=ind
                ind+=1
                ans.append([strs[i]])
        return ans