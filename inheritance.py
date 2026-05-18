class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

        def printname(self):
            print(self.firstnme, self.lastname)

            x = person("John", "Doe")
            x.printname()

            class student(person):
                pass

            x = Student("mike", "Olsen")
            x.printname()
        