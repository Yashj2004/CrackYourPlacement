class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[0]*(len(nums)+1)
        print(len(nums))
        for i in nums:
            a[i]+=1
        print(a)
        b=[]
        for i in range(len(a)):
            if a[i]>1:
                b.append(i)
        return b
