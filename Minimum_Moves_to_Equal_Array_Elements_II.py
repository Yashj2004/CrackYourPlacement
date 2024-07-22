class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid=nums[len(nums)//2]
        count=0
        for i in nums:
            count+=abs(mid-i)
        return count
