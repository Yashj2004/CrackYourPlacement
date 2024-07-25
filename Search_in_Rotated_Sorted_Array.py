class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            
            mid=(left+right)//2
            print(mid)
            if nums[mid]==target:
                return mid

            elif nums[left]<=nums[mid]:
                if nums[mid]<target or target < nums[left]:
                    left=mid+1
                else:
                    right=mid-1

            else:
                if nums[mid]>target or target > nums[right]:
                    right=mid-1
                else:
                    left=mid+1

        return -1
