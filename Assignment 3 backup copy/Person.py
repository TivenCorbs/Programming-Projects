class Person:

    def __init__(self,newName = "none",address = "none",phone = "999-999-9999"): # class constructor
        self.name = newName
        self.phone = phone
        self.address = address
        self.next = None
        self.prev = None

    def __eq__(self,other):
        if (isinstance(other, Person)):
            return(self.getphone()==other.getphone())
        if(isinstance(other,str)):
            return(self.getphone==other)
        else:
            return False
        


    def __str__(self):
        return "Name" + self.name + "address"+ self.address +"phone" + self.phone
    
    
    def setName(self,name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setPhone(self,phone):
        self.phone = phone
    


    def getName(self):
        return(self.name)
    
    def getAddress(self):
        return(self.address)
    
    def setPhone(self):
        return(self.phone)
    
    def getPhone(self):
        return(self.phone)
    
    
    
    








    





        
