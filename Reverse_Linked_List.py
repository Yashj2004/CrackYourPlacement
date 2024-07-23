# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        ptr=head
        while ptr is not None:
            ans.append(ptr.val)
            ptr=ptr.next
        ptr=head
        while ptr is not None:
            ptr.val=ans.pop()
            ptr=ptr.next
        return head
