class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        
        n1=[0 for i in range(26)]
        n2=[0 for i in range(26)]

        for i in range(len(s1)):
            n1[ord(s1[i])-ord('a')] += 1
            n2[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if n1[i] == n2[i] else 0)

        i = 0
        for j in range(len(s1),len(s2)):
            if(matches == 26):
                return True
            index1 = ord(s2[j]) - ord('a')
            index2 = ord(s2[i]) - ord('a')
            n2[index1] += 1
            
            if n1[index1] == n2[index1]: # matches after 1 is added
                matches += 1
            elif n1[index1]+1 == n2[index1]: # check if macthes before 1 is added to n2
                matches -= 1

            n2[index2] -= 1
            if n1[index2] == n2[index2]:
                matches += 1
            elif n1[index2] == n2[index2]+1:
                matches -= 1
            i+=1
        return matches == 26
            