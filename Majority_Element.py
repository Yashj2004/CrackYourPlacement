class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        a=0
        for i in range(n):
            if i==0:
                a+=1
            elif nums[i]==nums[i-1]:
                a+=1
            elif nums[i]!=nums[i-1]:
                if a>n/2:
                    return nums[i-1]
                else:
                   a=1
            if a>n/2:
                return nums[i-1]
        return 0
