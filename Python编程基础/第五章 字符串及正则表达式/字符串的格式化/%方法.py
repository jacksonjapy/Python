# if __name__ == '__main__':
#
#     name = 'tutu'
#     age = 18
#     height = 1.654
#     print("我的名字是" + "%s" % name, "，年龄是", "%d" % age, "，身高是" + "%.2f" % height + "m")
#     print("我的名字是%s,年龄是%d,身高是%.2fm" % (name, age, height))
if __name__ == '__main__':

    companies = [[7, "百度", "https://www.baidu.com"],
                 [9, "淘宝", "https://www.taobao.com"],
                 [12, "京东", "https://www.jd.com"],
                 [13, "唯品会", "https://www.vip.com"]]
    for company in companies:
        # print("公司编号:%-5d公司名称:%-5s公司网址:%+5s" % (company[0], company[1], company[2]))
        print("公司编号:%-5d公司名称:%-5s公司网址:%+5s" % (tuple(company)))