from node import Node
from Person import Person
from Employee import Employee
from Student import Student

class LinkedList:


    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert(self, index, newNode):
        if (index == 0):
            newNode.next = self.head
            self.head = newNode
        else:
            prevNode = self.head

            counter = 1
            while(counter < index):
                prevNode = prevNode.next
                counter = counter+ 1
            newNode.next = prevNode.next
            prevNode.next = newNode
        self.size = self.size + 1

# 0 -> self.head = item0 -> 1 -> item1 -> 2 -> item2 -> 3 -> None
# newNode.next = self.head
# self.head = newNode 
# item0 -> newItem -> item1 -> item2 -> None


# Insert at 3
# i = 3

# j = 0
# temp = item0
# while 0 < 3
# temp = item1
# j = 0 + 1 = 1
# while 1 < 3
# temp = item2
# j = 1 + 1 = 2
# while 2 < 3
# temp = None !!!
# j = 2 + 1 = 3
# while 3 < 3
# n.next = temp.next (n.next = temp3.next = None)
    

    def length(self):  
        return(int(self.size))
    

    def add(self, n):
        
         if self.size == 0:
            self.head = n
         else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = n
         self.size = self.size + 1


            
            

    def delete(self, indexToDelete):
        if(indexToDelete==0):
            self.head = self.head.next
        else:
            i = 1
            prevNode = self.head
            nodeToDelete = self.head.next
            while i < indexToDelete:
                prevNode = prevNode.next
                nodeToDelete = nodeToDelete.next
                i = i + 1
                if (nodeToDelete == None):
                    return
            prevNode.next = nodeToDelete.next
            nodeToDelete.next = None
        
        self.size = self.size - 1



    def search(self, key):
        link = LinkedList()
        current = self.head
        index = 0
        while current:
            if current.data.getName() == key:
                newNode = Node(current.data)
                link.add(newNode) 
            current = current.next
            index = index + 1

        return link



    def __str__(self):
        stringtoReturn = ""
        node = self.head
        while(node != None): #loop over every node
            stringtoReturn + str(node) + "\n"
            node = node.next
        return(stringtoReturn)

    
    def __getitem__(self, e):
     currElement = self.head
     skippedOver = 0
     while(skippedOver < e):
            currElement = currElement.next
            skippedOver = skippedOver + 1 
     return(currElement)
    


    
        
   
if __name__=="__main__":
             
             sampleperson1 = Person("James","Beach City","122-334-121")

             sampleperson2 = Person("Gabriel","Los Angeles","510-332-121")
             sampleperson3 = Employee("Eric","New York","119-121-313","English")
             sampleperson4 = Employee("Tony","Manila","131-312-121","Math")
             sampleperson5 =Student("John","Tokyo","312-241-124","Senior")
             sampleperson6 =Student("Ai","Tokyo","112-333-444","Junior")
             sampleperson7 = Employee("Pepper","Las Vegas","132-444-131","Art")
             sampleperson8 = Person("Jack","Mexico City","555-332-121")
             
             linkedlist = LinkedList()
             n1 = Node(sampleperson1)
             linkedlist.add(n1)
             n2 = Node(sampleperson2)
             n3 = Node(sampleperson3)
             n4 = Node(sampleperson4)
             n5 = Node(sampleperson5)
             n6 = Node(sampleperson6)
             n7 = Node(sampleperson7)
             n8 = Node(sampleperson8)
             linkedlist.add(n2)
             linkedlist.add(n3)
             linkedlist.insert(0,n4)
             linkedlist.add(n5)
             linkedlist.insert(3,n6)
             linkedlist.delete(5)
             linkedlist.delete(1)
             linkedlist.delete(3)
             linkedlist.add(n7)
             linkedlist.insert(4,n8)
             print(linkedlist.length(), linkedlist.length() == 4)
             linkedlist.search(3)
             print(linkedlist.search(3))
             print(linkedlist.__str__())

#n4 --> (new head)
#n1(original head) --> deleted
#n2
#n6(insert) --> deleted
#n8
#n5 --> deleted --> n7 replaced
         
         

         
 




         
         

         
         
         
     
     
     
    
