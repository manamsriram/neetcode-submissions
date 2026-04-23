class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==1):
            return 0
        min=prices[0]
        ans=0
        for i in range(1,len(prices)):
            if(prices[i]>min and ans<prices[i]-min):
                ans=prices[i]-min
            if(min>prices[i]):
                min=prices[i]
        return ans