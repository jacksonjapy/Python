if __name__ == '__main__':
    a = "四川信息职业技术学院 >>> www.scitc.com.cn"
    ikun = a.split() #使用默认分割符
    print(ikun)
    #使用 > 作为分隔符
    se_ikun = a.split(">")
    print(se_ikun)
    #分割出学校名和网址
    th_ikun = a.split(">>>")[1].split(".")
    print(th_ikun)

    kunkun = "学python了：@张三@李四@王五@赵六"
    wangkun = kunkun.split("：")[1].split("@")
    del wangkun[0]
    print(wangkun)