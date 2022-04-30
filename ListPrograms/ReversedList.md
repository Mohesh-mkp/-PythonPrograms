
class node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def insert(self,val):
        node_obj=node(val)
        if self.head is None:
            self.head=node_obj
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node_obj
            temp=temp.next
    
    def reverse(self):
        prev=None
        cur=self.head
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        self.head=prev
        
    def disp(self):
        cur=self.head
        while cur:
            print(cur.data, end="-->")
            cur=cur.next

my_list=LinkedList()
length=int(input("Enter length of list: "))
for i in range(0,length):
    val=int(input("Enter number to list: "))
    my_list.insert(val)

my_list.reverse()
my_list.disp()


