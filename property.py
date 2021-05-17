

class Email:
    def __init__(self, type, number):           # Initializer method
        self.type = type                        # Initializes an already Constructed instance obj
        self._number = number
        self._subject = "no reply"              # Indicates that attributes isn't public

    @property                                   # Decorator
    def details(self):                          # The method will act as an attribute now
        return self._number    

                                                # But no value can be assigned in the property without using seeter method !
    @details.setter
    def details(self, num):
        self.number = num               

    @details.deleter                            # Confirmation whenever a method is deleted
    def details(self):
        print("Detail deleted !")


e1 = Email("Spam", 4)                       
e2 = Email("Promotional", 5) 

e1.details                                      # Accessed without giving '()'
e2.details = 7

print(e2.details)

del e2.details                                  
print(e2.details)


