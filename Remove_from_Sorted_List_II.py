# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans={}
        ptr=head
        while ptr:
            if ptr.val not in ans.keys():
                ans[ptr.val]=1
            else: 
                ans[ptr.val]+=1
            ptr=ptr.next

        
        while head and ans[head.val]>1:
            head=head.next
        ptr=head
        while ptr and ptr.next:
            if ans[ptr.next.val]>1:
                    ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return head
