# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        def inshow(root):
            if root== None:
                return 
            if root.left is not None:
                inshow(root.left)
            self.ans.append(root.val)
            if root.right is not None:
                inshow(root.right)
        inshow(root)
        return self.ans
