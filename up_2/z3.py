class Two_nums:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def show_nums(self):
        print(self.num1, self.num2)

    def change_nums(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2

    def nums_sum(self):
        print(self.num1 + self.num2)

    def nums_max(self):
        print(max(self.num1, self.num2))

nums = Two_nums(1, 2)
nums.show_nums()
nums.change_nums(3, 4)
nums.nums_sum()
nums.nums_max()