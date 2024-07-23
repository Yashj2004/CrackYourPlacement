# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans=[]
        ptr=head
        while ptr is not None:
            ans.append(ptr.val)
            ptr=ptr.next
        return ans==ans[::-1]
