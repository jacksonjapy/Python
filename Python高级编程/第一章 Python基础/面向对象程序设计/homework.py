# 类的创建和使用：
# （1）创建一个Animal类
# 自定义一个__init__()方法，用于初始化一下实例属性：color(颜色)、age(年龄)
class Animal:
    count = 0

    def __init__(self, color, age):
        self.color = color
        self.age = age
        Animal.count += 1

    # 自定义一个名为move的实例方法，用于描述动物移动的行为。
    def move(self):
        print("moving...")

    # 自定义一个名为count_nums的类方法，用于统计动物的数量。
    @staticmethod
    def count_nums():
        print(f"现有{Animal.count}个实例。")

    # 自定义一个名为info的静态方法，用于显示Animal类的作用。
    @staticmethod
    def __info(self):
        print("Animal Class is running...")

    # 自定义一个__del__()方法，完成对象的删除。

    def __del__(self):
        print(f"正在删除实例")


# （2）创建一个Dog子类，其继承于Animal类
class Dog(Animal):
    # 重写__init__()方法，给Dog类添加以下几个属性：
    # name(名称)、eyes(眼睛数)、nose(鼻子数)、ears(耳朵数)、mouth（嘴巴数）、legs（腿的数量）
    def __init__(self, color, age, name, eyes, nose, ears, mouth, legs):
        Animal.__init__(self, color, age)
        self.name = name
        self.eyes = eyes
        self.nose = nose
        self.ears = ears
        self.mouth = mouth
        self.legs = legs

    # 添加一个新的实例方法名为run(),表示Dog的奔跑行为。
    def run(self):
        print(f"{self.name} is running...")


if __name__ == '__main__':
    # （3）在主程序中，创建两个Dog类的对象，并查看对象的颜色，调用run()方法和count_nums()方法
    Golden_retriever = Dog("yellow", 10, "Golden retriever", 2, 1, 2, 1, 4)
    Labrador = Dog("white", 10, "Labrador", 2, 1, 2, 1, 4)
    print(f"金毛的颜色是{Golden_retriever.color}，拉布拉多的颜色是{Labrador.color}。")
    Golden_retriever.run()
    Labrador.run()
    Golden_retriever.count_nums()
    Labrador.count_nums()
