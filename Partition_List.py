# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        part=[]
        rem=[]
        ptr=head
        while ptr:
            if ptr.val<x:
                part.append(ptr.val)
            else:
                rem.append(ptr.val)
            ptr=ptr.next
        ptr=head
        i=0
        while i<len(part):
            ptr.val=part[i]
            i+=1
            ptr=ptr.next
        i=0
        while i<len(rem):
            ptr.val=rem[i]
            i+=1
            ptr=ptr.next
        return head
