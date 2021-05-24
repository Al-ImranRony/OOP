

print(issubclass(str, object))
print(issubclass(int, object))

class Person:
    def __init__(self, name, age, contact, address):
        self.name = name
        self.age = age
        self.contact = contact
        self.address = address

    def is_adult(self):
        if self.age < 18:
            return False
        else:
            return True

    def addresses(self):
        print(self.address)


class Employee(Person):
    def __init__(self, name, age, contact, address, salary, officeAddress):
        super().__init__(name, age, contact, address)                       # super(), uses to call base class method
        self.salary = salary
        self.officeAddress = officeAddress

    def tax(self):
        if self.salary > 50000:
            return self.salary * 0.05
        else: 
            return 0

    def addresses(self):                                                    # Method overridden
        print("Home:", self.address, "- Office:", self.officeAddress)

    

emp1 = Employee("Aman", 26, 88019, "Jessore", 50000, "Mohakhali")

print(emp1.name, emp1.age, emp1.contact)
print(emp1.is_adult())
print(emp1.addresses())

print(isinstance(emp1, Person))
print(issubclass(Employee, Person))

print(issubclass(Person, object))