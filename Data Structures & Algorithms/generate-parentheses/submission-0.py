class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def par(n,s,st,oc,cc,i):
            if(oc==n and cc==n):
                for i in s:
                    st+=i
                ans.append(st)
            if(oc<n):
                s[i]='('
                par(n,s,st,oc+1,cc,i+1)
            if(cc<oc):
                s[i]=')'
                par(n,s,st,oc,cc+1,i+1) 
        s=[' ']*(n+n)
        st=''
        ans=[]
        par(n,s,st,0,0,0)
        return ans