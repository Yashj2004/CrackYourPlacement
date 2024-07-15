class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=len(nums)-1
        while i>=0:
            if len(nums)<=1:
                break
            if nums[i]==nums[i-1]:
                nums[i-1]=nums[i]
                nums.remove(nums[i])
            i-=1
        return len(nums)
