class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        j=1
        i=0
        while j<(len(prices)):
            if prices[i] < prices[j]:
                if a<(prices[j] - prices[i]):
                    a=prices[j] - prices[i]
            if prices[i] > prices[j]:
                i=j
            j+=1
        return a
