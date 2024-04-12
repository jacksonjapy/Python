# 创建类
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


# 创建对象（实例）
if __name__ == '__main__':
    # 在类外，可以通过 “对象名.方法名”Object.method 来访问类中的方法。
    ikun = Person("ikun", "男", 18)
    ikun.show_information()
    ikun.walk()
    ikun.modify("李四")

    yym = Person("叶银民", "男", 20)
    yym.show_information()
    yym.walk()
    yym.show_count()  # 通过实例调用类中的方法
    Person.show_count()  # 通过类调用类中的方法
    Person.info_print()  # 通过类调用类中的静态方法
# 自动调用了__del__方法
# 手动删除对象
    del ikun
    Person.show_count()
    del yym
# 构造：创建
# 析构：销毁(删除)
"""
A method in Python is a function that is defined within a class and operates on an instance (or object) of that class. 
It has access to the instance's attributes and can modify or use them as needed. 
Methods are used to implement the behavior of objects and are typically called by attaching the method name to an object reference,allowing for actions specific to that object.
In more technical terms: Methods in Python are bound functions that are associated with a particular class instance. 
They have the ability to access and manipulate the state of the instance through the self parameter which refers to the instance itself. 
When a method is invoked on an object, self is automatically passed as the first argument, providing the method with access to the object's attributes and other methods.
Python中的方法是在类中定义并对该类的实例（或对象）进行操作的函数。
它可以访问实例的属性，并可以根据需要修改或使用这些属性。
方法用于实现对象的行为，通常通过将方法名称附加到对象引用来调用，从而允许特定于该对象的操作。
用更专业的术语来说：Python中的方法是与特定类实例关联的绑定函数。
它们能够通过引用实例本身的self参数来访问和操作实例的状态。
当对对象调用方法时，self会自动作为第一个参数传递，从而为该方法提供对对象属性和其他方法的访问权限。
"""
