class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def par(oc,cc):
            if(oc==n and cc==n):
                ans.append(''.join(s))
            if(oc<n):
                s.append('(')
                par(oc+1,cc)
                s.pop()
            if(cc<oc):
                s.append(')')
                par(oc,cc+1)
                s.pop()
        s=[]
        ans=[]
        par(0,0)
        return ans