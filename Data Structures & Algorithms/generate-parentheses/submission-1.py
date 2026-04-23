class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def par(n,s,oc,cc,i):
            if(oc==n and cc==n):
                ans.append(''.join(s))
            if(oc<n):
                s[i]='('
                par(n,s,oc+1,cc,i+1)
            if(cc<oc):
                s[i]=')'
                par(n,s,oc,cc+1,i+1) 
        s=[' ']*(n+n)
        st=''
        ans=[]
        par(n,s,0,0,0)
        return ans