# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ans=[]
        ptr=head
        while ptr:
            ans.append(ptr.val)
            ptr=ptr.next
        left=0
        right=len(ans)-1
        res=[]
        while left<=right:
            res.append(ans[left])
            res.append(ans[right])
            left+=1
            right-=1
        ptr=head
        i=0
        while ptr:
            ptr.val=res[i]
            i+=1
            ptr=ptr.next
        return head
