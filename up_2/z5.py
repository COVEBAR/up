class Person:
    def __init__(self, name="User", age=0):
        self.name = name
        self.age = age
        print("Hello,", self.name, self.age)

    def __del__(self):
        print("Bye-bye,", self.name, self.age)

tom = Person("Tom", 23)
nobody = Person()