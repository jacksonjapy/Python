'''if __name__ == '__main__':
    num = 5
    a = list(map(int,input("请输入"+str(num)+"个整数：").split(";")))
    print(a)'''
'''if __name__ == '__main__':
    a = 10
    b = 20
    # print(a,b)
    print(a,b,sep=",",end="")'''
'''if __name__ == '__main__':
    a = list(range(1,11))
    for prin in a:
        print(prin,end=" ")'''
#文件写入操作
if __name__ == '__main__':
    a,b = map(int,input("请输入两个整数：").split(","))
    #print(a,b,sep=",")
    result1 = a + b
    result2 = a - b
    path = r"/home/jackson/桌面/out.txt"
    f = open(path,"w")
    print(f"{a}+{b}={result1}",file=f)
    print(f"{a}-{b}={result2}",file=f)
    f.close()