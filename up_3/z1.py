class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        print(self.rate * self.days)

miner = Worker("Steve", "Minecraftov", 64, 16)
print(miner.name, miner.surname, miner.rate, miner.days)
miner.GetSalary()