from Person import Person
class Student(Person):

    def __init__(self,newName="none", address="none", phone="999-999-9999", year=9999):
        super().__init__(newName,address,phone)
        self.year = year
 
    def getGraduationYear(self):
        return (self.year)
    
    def setGraduationYear(self,year):
        self.year = year

    def __str__(self) -> str:
        return super().__str__() + "Year:" + str(self.year)


        



    


        