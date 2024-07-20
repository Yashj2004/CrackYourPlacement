class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum=[]
        cur=0
        for i in nums:
            cur+=i
            self.prefix_sum.append(cur)
    def sumRange(self, left: int, right: int) -> int:
        right_sum=self.prefix_sum[right]
        left_sum=self.prefix_sum[left-1] if left>0 else 0
        return right_sum-left_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
