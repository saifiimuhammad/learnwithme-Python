class Employee:
    # salary = 0

    # Constructor
    def __init__ (self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        print(f"Employee {name} is created with salary {salary} and position {position}") # f-string

    # Methods
    def getSalary (self):
        print(f"Salary is {self.salary}")
    def setSalary (self, salary):
        self.salary = salary




saif = Employee('Saif', 71000, 'Manager')
sarim = Employee('Sarim', 55000, 'Developer')
abdullah = Employee('Abdullah', 15000, 'Intern')

