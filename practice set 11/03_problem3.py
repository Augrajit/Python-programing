class Employee:
    salary=20000
    increment=10

    @property

    def salaryAfterIncrement (self):
        return (self.salary+self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter

    def salaryAfterIncrement (self,salary):
        self.increment=((salary/self.salary)-1)*100#old salary=salary,new salary=self.salary

e=Employee()
print(e.salaryAfterIncrement)   
e.salaryAfterIncrement=28000
print(e.increment)