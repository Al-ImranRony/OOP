class Email:
    def __init__(self, type, number):           # Initializer method
        self.type = type                        # Initializes an already Constructed instance obj
        self.number = number
        self._subject = "no reply"              # Indicates that attributes isn't public


    def _details(self, type, number):           # Indicates Hidden Private method  
        self.type = type                        #Instance Variable
        self.number = number

    def send(self):
        print("Msg sent.")

    def receive(self):
        print("Msg received.")


print(id(e1), type(e2))

e1 = Email("Spam", 4)                       # Intantiated
e2 = Email("Promotional", 5)                # e1, e2 are instance objects

e2.name = "Promotional"                     # Instance Variable
print(e2.name)
print(e2._subject)                          # Private attribute which Can be accessed, but shouldn't


# e1.details("Spam", 4)
# e2.details("Promotional", 5)

e1.send()
e2.receive()

print(e1.type)
print(e2.number)