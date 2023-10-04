
class Node:
    def __init__(self,n):
        self.next     = None
        self.data     =  n 
        

    def getData(self):
        return(self.data)

    def getNext(self):
        return(self.next)

    def setData(self, d):
        self.data = d

    def setNext(self, n):
        self.next = n

    def __str__(self):
        return(self.data)

    