class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end=len(nums)-1
            while start<end:
                a=nums[i]+nums[start]+nums[end]
                if a>0:
                    end-=1
                elif a<0:
                    start+=1
                else:
                    ans.append([nums[i],nums[start],nums[end]])
                    start+=1
                    while  nums[start]==nums[start-1] and start< end:
                        start+=1
        return ans
