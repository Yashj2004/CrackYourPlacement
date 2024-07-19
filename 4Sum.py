class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if  i>0 and nums[i]==nums[i-1]:
                    continue
            for j in range(i+1,len(nums)):
                if  j>i+1 and nums[j]==nums[j-1]:
                    continue
                start=j+1
                end=len(nums)-1
                while start < end:
                    total=nums[i]+nums[j]+nums[start]+nums[end]
                    if total > target:
                        end-=1
                    elif total < target:
                        start+=1
                    else :
                        ans.append([nums[i],nums[j],nums[start],nums[end]])
                        start+=1
                        while nums[start]==nums[start-1] and start<end:
                            start+=1
        return ans
