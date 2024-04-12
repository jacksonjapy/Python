#导入整个模块
'''import math

if __name__ == '__main__':
    num = math.sqrt(9)
    print(num)'''

#导入时添加别名
'''import math as sx

if __name__ == '__main__':
    num = sx.sqrt(9)
    print(num)'''

#只导入某个模块中的某一个函数
'''from math import sqrt

if __name__ == '__main__':
    num = sqrt(9)
    print(num)'''

#只导入某个模块中某一个函数时添加别名
'''from math import sqrt as kf

if __name__ == '__main__':
    num = kf(9)
    print(num)'''