class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        left=1
        right=1
        n=len(nums)
        l_arr=[0]*n
        r_arr=[0]*n
        for i in range(len(nums)):
            j=-i-1
            l_arr[i]=left
            r_arr[j]=right
            left*=nums[i]
            right*=nums[j]
        return [l*r for l,r in zip(l_arr,r_arr)]
