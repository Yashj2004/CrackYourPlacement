# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        c=0
        while ptr:
            c+=1
            ptr=ptr.next
        if c==1 and n==1:
            return None
        
        n=c-n
        a=0
        if n==0:
            head=head.next
        ptr=head
        while ptr and ptr.next :
            if a==n-1:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
            a+=1
        return head

        

       
