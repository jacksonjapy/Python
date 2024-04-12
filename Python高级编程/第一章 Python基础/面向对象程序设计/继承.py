# 父类
class Person:
    """
    类的说明
    """
    # 类体（数据、行为）
    # 类的属性（通常情况下时通过类名.属性名来访问）
    count = 0  # 统计对象的数量

    def __init__(self, in_name, in_sex, in_age):  # 默认的类初始化方法（构建函数__init__）
        # 实例属性
        self.name = in_name
        self.sex = in_sex
        self.age = in_age
        print(f'初始化了一个{self.name}的方法，性别：{self.sex}，年龄：{self.age}')
        Person.count += 1  # 每创建一个对象，count就加1

    # 自定义方法（实例化方法）
    def show_information(self):
        print(f'姓名：{self.name}，性别：{self.sex}，年龄：{self.age}')

    def walk(self):
        print(f'{self.name}正在走路！')

    def modify(self, in_name):
        print(f'正在修改一个{self.name}的方法！')
        self.name = in_name
        print(f'修改后的姓名：{self.name}，性别：{self.sex}，年龄：{self.age}')

    def __del__(self):  # 默认的类销毁(删除)方法，可以自定义 (析构函数__del__)
        print(f'正在销毁(删除)一个{self.name}的方法！')
    # 在类中，可以通过__self__来访问类中的属性。
        Person.count -= 1

    # 定义类方法
    @classmethod  # 类方法
    def show_count(cls):
        print(f'现在共有{cls.count}个实例')

    # 定义静态方法
    @staticmethod
    def info_print():
        print("This is a Person Class.")


class Student(Person):  # student继承与Person类
    """
    学生类
    """
    def study(self):
        print(f'{self.name}正在学习！')


if __name__ == '__main__':
    stu1 = Student('张三', '男', 18)  # 调用从父类中继承的构造方法(__init__)
    stu2 = Student('李四', '女', 19)
    stu1.study()
