if __name__ == '__main__':
    # name = 'tutu'
    # age = 18
    # height = 1.654
    # print("我的名字是{:s}，年龄是{:d}，身高是{:.2f}m。".format(name, age, height))
    companies = [[7, "百度", "https://www.baidu.com"],
                 [9, "淘宝", "https://www.taobao.com"],
                 [12, "京东", "https://www.jd.com"],
                 [13, "唯品会", "https://www.vip.com"]]

    for i in companies:
        print("公司编号：{0[0]:<3d}公司名称：{0[1]:<5s}公司网址：{0[2]:s}".format(i))
        print("公司编号：{:<3d}公司名称：{:<5s}公司网址：{:s}".format(i[0], i[1], i[2]))
        print("公司编号：{:<3d}公司名称：{:<5s}公司网址：{:s}".format(*i))
