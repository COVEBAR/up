class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_rate(self):
        return self.__rate
    def get_days(self):
        return self.__days

    def GetSalary(self):
        print(self.__rate * self.__days)

miner = Worker("Steve", "Minecraftov", 64, 16)
print(miner.get_name(), miner.get_surname(), miner.get_rate(), miner.get_days())
miner.GetSalary()