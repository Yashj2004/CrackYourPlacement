# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans=""
        ptr=head
        while ptr :
            ans+=str(ptr.val)
            ptr=ptr.next
        return int(ans,2)
