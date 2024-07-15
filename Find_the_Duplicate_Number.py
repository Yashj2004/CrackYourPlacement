class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       a=[False]*(len(nums)+1)
       for i in nums:
        if a[i]==True:
            return i
        if a[i]==False:
            a[i]=True
