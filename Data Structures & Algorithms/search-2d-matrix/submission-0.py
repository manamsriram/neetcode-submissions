class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        i,j=0,(m*n)-1
        while(i<=j):
            a=i+((j-i)//2)
            l,h=(a//n),(a%n)
            if(matrix[l][h]==target):
                return True
            elif(matrix[l][h]<target):
                i=a+1
            else:
                j=a-1
        return False        