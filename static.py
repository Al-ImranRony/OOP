
class Employee:
    dept = "SD"                                     # Class/static variable

    def __init__(self, name, id):
        self.name = name
        self.id = id

    @staticmethod
    def salary(amount):
        return amount


emp1 = Employee("Ron", 531)
emp2 = Employee("Jon", 530)

print(emp1.dept)
print(emp2.dept)
print(emp2.name)
print(emp1.id)

print(Employee.dept)                                # Accessing static variable using the class name

emp1.dept = "SQA"
print(emp1.dept, emp2.dept)

Employee.dept = "ML"                                # Observe, how static variable can be accessed
print(Employee.dept, emp1.dept, emp2.dept)


print(Employee.salary(0000))                        # Accessing static method
print(emp1.salary(50000))