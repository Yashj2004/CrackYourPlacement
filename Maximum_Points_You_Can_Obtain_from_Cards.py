class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_l=sum(cardPoints[:k])
        sum_r=0
        res=sum_l
        for i in range(k):
            sum_l-=cardPoints[k-1-i]
            sum_r+=cardPoints[len(cardPoints)-1-i]
            res=max(res,sum_l+sum_r)
        return res
