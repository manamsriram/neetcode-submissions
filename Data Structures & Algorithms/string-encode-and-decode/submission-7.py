class Solution:
    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+'#'+i
        return s

    def decode(self, s: str) -> List[str]:
        str=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!='#'):
                j+=1
            l=int(s[i:j])
            i=j+1
            j=i+l
            str.append(s[i:j])
            i=j
        return str