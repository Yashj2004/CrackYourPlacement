class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        pre_cut=defaultdict(int)
        pre_cut[0]=1
        res=0
        for i in nums:
            prefix_sum+=i
            rem=prefix_sum % k
            if rem in pre_cut:
                res+=pre_cut[rem]
            pre_cut[rem]+=1
        return res
        
