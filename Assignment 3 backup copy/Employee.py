from Person import Person
class Employee(Person):
    def __init__(self,newName = "none",address = "none",phone = "999-999-9999",department = "not assigned"):
         super().__init__(newName,address,phone)
         self.department = department
    
    
    def getDepartment(self):
         return self.department
    
    def setDepartment(self,department):
         self.department = department

    def __str__(self) -> str:
         return super().__str__() + "Department" + self.department
    
    