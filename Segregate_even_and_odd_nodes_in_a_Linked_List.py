class node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next
class linked_list:
  def __init__(self):
    self.head=None

  def insert(self,data):
    node1=node(data,self.head)
    self.head=node1

  def segreagte_even_odd(self):
    even=[]
    odd=[]
    ptr=self.head
    while ptr:
      if ptr.data%2==0:
        even.append(ptr.data)
      else:
        odd.append(ptr.data)
      ptr=ptr.next
    ptr=self.head
    i=0
    while i<len(even):
      ptr.data=even[i]
      i+=1
      ptr=ptr.next
    i=0
    while i<len(odd):
      ptr.data=odd[i]
      i+=1
      ptr=ptr.next

  def display(self):
    ptr=self.head
    ans=""
    while ptr is not None:
      ans+=str(ptr.data)+"-->"
      ptr=ptr.next
    ans+='Null'
    return ans

llist = linked_list()
llist.insert(6)
llist.insert(7)
llist.insert(1)
llist.insert(4)
llist.insert(5)
llist.insert(10)
llist.insert(12)
llist.insert(8)
llist.insert(15)
llist.insert(17)

print ("Linked List before sorting")
print(llist.display())

llist.segreagte_even_odd()

print ("Linked List after sorting")
print( llist.display())
