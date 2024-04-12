print("请输入一个整数：")
a = int(input())
print("请输入模？")
m = int(input())

if a < m:
    a, m = m, a
    x1, x2,x3= 1, 0, a
    y1, y2,y3= 0, 1, m
    while y3 != 0:
        Q = x3//y3
        t1, t2, t3 = x1 - Q*y1, x2 - Q*y2, x3 - Q*y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    print(x2)
else:
    x1, x2, x3 = 1, 0, a
    y1, y2, y3 = 0, 1, m
    while y3 != 0:
        Q = x3 // y3
        t1, t2, t3 = x1 - Q*y1, x2 - Q*y2, x3 - Q*y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    print(x1)
