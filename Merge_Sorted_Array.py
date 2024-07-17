class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=n-1
        p=m-1
        j=len(nums1)-1
        while p>=0 and j>p:
            if nums2[i]>nums1[p]:
                nums1[j]=nums2[i]
                i-=1
                j-=1
            else:
                nums1[j]=nums1[p]
                p-=1
                j-=1
        while i>=0:
            nums1[j]=nums2[i]
            i-=1
            j-=1

            
        
