class Animal:
    count = 0

    def __init__(self, color, age):
        self.color = color
        self.age = age
        Animal.count += 1

    def move(self):
        print("moving...")

    def count_nums(self):
        print(f"现有{Animal.count}个实例。")

    def __info(self):
        print("Animal Class is running...")

    @staticmethod
    def __del__(self):
        print(f"正在删除实例")
