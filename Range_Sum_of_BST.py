# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum=0
        def travers(root,low,high):
            if root.val>=low and root.val<=high:
                self.sum+=root.val
            if root.left:
                travers(root.left,low,high)
            if root.right:
                travers(root.right,low,high)
        travers(root,low,high)
        return self.sum
