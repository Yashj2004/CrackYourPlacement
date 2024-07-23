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

  def sort_linked_list(self):
    ptr=self.head
    count=[0,0,0]
    while ptr is not None:
      count[ptr.data]+=1
      ptr=ptr.next

    ptr=self.head
    i=0
    while ptr is not None:
      if count[i]==0:
        i+=1
      ptr.data=i
      ptr=ptr.next
      count[i]-=1

  def display(self):
    ptr=self.head
    ans=""
    while ptr is not None:
      ans+=str(ptr.data)+"-->"
      ptr=ptr.next
    ans+='Null'
    return ans

llist = linked_list()
llist.insert(0)
llist.insert(1)
llist.insert(0)
llist.insert(2)
llist.insert(1)
llist.insert(1)
llist.insert(2)
llist.insert(1)
llist.insert(2)

print ("Linked List before sorting")
print(llist.display())

llist.sort_linked_list()

print ("Linked List after sorting")
print( llist.display())


