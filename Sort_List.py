# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        ptr=head
        while ptr:
            ans.append(ptr.val)
            ptr=ptr.next
        ans.sort()
        print(ans)
        i=0
        ptr=head
        while ptr:
            ptr.val=ans[i]
            i+=1
            ptr=ptr.next
        return head
