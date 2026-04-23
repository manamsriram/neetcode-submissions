class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bs(a,i,j,x):
            while(i<=j):
                mid=(i+j)//2
                if(a[mid]>x):
                    j=mid-1
                elif(a[mid]<x):
                    i=mid+1
                else:
                    return mid
            return -1

        for i in range(len(numbers)):
            x=target-numbers[i]
            print(x)
            if(x>=numbers[i]):
                y=bs(numbers,i,len(numbers)-1,x)
            else:
                y=bs(numbers,0,i,x)
            print(y)
            if(y!=-1 and i!=y):
                return [i+1,y+1]