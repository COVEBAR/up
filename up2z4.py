class Counter:
    def __init__(self, start=0):
        self.counting = int(start)
    def count_p(self):
        self.counting += 1
    def count_m(self):
        self.counting -= 1
    def print_counter(self):
        print(self.counting)

a_plus_e_minus = counter(int(input("Start: ")))
text = input("Text: ")
for i in text:
    if i == "a":
        a_plus_e_minus.count_p()
    elif i == "e":
        a_plus_e_minus.count_m()
a_plus_e_minus.print_counter()
a_plus_e_minus = counter()
for i in text:
    if i == "a":
        a_plus_e_minus.count_p()
    elif i == "e":
        a_plus_e_minus.count_m()
a_plus_e_minus.print_counter()