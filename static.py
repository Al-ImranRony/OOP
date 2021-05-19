
class Employee:
    dept = "SD"                                     # Class/static variable
    count = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Employee.count += 1

    @classmethod                                    # class method
    def department(cls):                            # class method can only access class variables because of no self arg.
        return cls.dept                             # cls is the short form of Class which is a convention

    @classmethod
    def show_count(cls):
        print("Total employees: ", cls.count)

    @staticmethod                                   # Static method most often works with logic neither use class variables nor instance variables
    def status(id):
        print("Valid Employee") if (id > 500) else print("Employee not valid !")
            
        


Employee.show_count()

emp1 = Employee("Ron", 531)
emp2 = Employee("Jon", 530)

Employee.show_count()

print(emp1.dept)
print(emp2.dept)
print(emp2.name)
print(emp1.id)

print(Employee.dept)                                # Accessing class variable using the class name


# Observe the id's of the variable, they will be similar to each others
print("ID's of class variable: ", id(Employee.dept), id(emp1.dept), id(emp2.dept)) 

emp1.dept = "SQA"
print(emp1.dept, emp2.dept)

Employee.dept = "ML"                                # Observe, how class variable can be accessed
print(Employee.dept, emp1.dept, emp2.dept)

print(Employee.department())                        # Accessing class method with class

Employee.show_count()
Employee.status(531)                                # Accessing static method with class