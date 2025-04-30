class Train:
    def __init__(self, place, num, time):
        self.place = place
        self.num = num
        self.time = time
    def train_info(self):
        if self.num == int(input("Train num: ")):
            print(self.num, self.place, self.time, sep="\n")
train123 = Train("Novosibirsk", 123, "12:34")
train123.train_info()