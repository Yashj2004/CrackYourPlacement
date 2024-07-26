# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i=1
        ptr=head
        ans=[]
        while ptr:
            if i>=left and i<=right:
                ans.append(ptr.val)
            ptr=ptr.next
            i+=1
        ans=ans[::-1]
        ptr=head
        i=1
        a=0
        while ptr:
            if i>=left and i<=right:
                ptr.val=ans[a]
                a+=1
            ptr=ptr.next
            i+=1
        return head
