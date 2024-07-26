# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        var1=[]
        var2=[]

        ptr1=l1
        while ptr1:
            var1.append(ptr1.val)
            ptr1=ptr1.next

        ptr2=l2
        while ptr2:
            var2.append(ptr2.val)
            ptr2=ptr2.next

        var1=var1[::-1]
        var2=var2[::-1]

        carry=0
        ans=[]
        i=0
        while i<max(len(var1),len(var2)) or carry!=0:
            a=var1[i] if i<len(var1) else 0
            b=var2[i] if i<len(var2) else 0

            val=a+b+carry
            rem=val%10
            carry=val//10

            ans.append(rem)
            i+=1
        ans=ans[::-1]
        head=ListNode()
        last=head
        i=0
        while i<len(ans):
            node=ListNode(ans[i])
            last.next=node
            last=last.next
            i+=1
        return head.next
