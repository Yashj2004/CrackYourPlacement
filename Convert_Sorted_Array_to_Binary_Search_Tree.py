# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(nums,start,end):
            if start>end:
                return
            mid=int((start+end)/2)
            root=TreeNode(nums[mid])
            root.left=build_tree(nums,start,mid-1)
            root.right=build_tree(nums,mid+1,end)
            return root
        return build_tree(nums,0,len(nums)-1)
