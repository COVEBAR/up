import random

class Student:
    def __init__(self, sname, bday, group, performance):
        self.sname = sname
        self.bday = bday
        self.group = group
        self.performance = performance
    def change_info(self):
        self.sname = input("Surname: ")
        self.bday = input("Date of birth: ")
        self.group = int(input("Group: "))
    def print_info(self):
        print(self.sname)
        print(self.bday)


person = Student("Malinovsky", "24.06.2007", 632, [random.randint(2, 5) for _ in range(5)])
person.change_info()
person.print_info()