class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        i=0
        j=0
        while j<len(prices):
                
            if j==len(prices)-1 or prices[j]>prices[j+1]:
                ans+=(prices[j]-prices[i])
                i=j+1

            j+=1
        
        return ans
