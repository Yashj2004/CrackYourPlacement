class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        while i<len(nums) and nums[i]!=0:
            i+=1
        for j in range (i,len(nums)):
            if len(nums)<=1:
                break
            if i<len(nums) and nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1       
