import string

if __name__ == '__main__':
    # 1.假设一段英文，如"i love Programming, I love python",请编程将英文的首字母大写，其余小写。
    english_str = "i love Programming, I love python"
    print(english_str.title())

    # 2.请编程将列表["张三","李四","王五"]按如下格式输出。
    list_str = ["张三", "李四", "王五"]
    python_class = "上Python课了："

    # 依次从列表中取出元素，每次取出来后在元素前打印一个@符号
    print(python_class + "@".join(list_str))
    # 3.请编程删除"    i love Programming, I love python    "字符串中前后多余的空格。
    str_str = "    i love Programming, I love python    "
    print(str_str.strip())

    # 4. (简答题) 请编程将字符串"I like china, I love China, ChIna is great."中所有写错了的"China"单词修改正确，即改为"I like China, I love China, China is great."
    oringin_str = "I like china, I love China, ChIna is great."
    error_str = "ChIna"
    right_str = "China"
    print(oringin_str.replace("ChIna", "China"))

    # 5. (简答题)对以下两个列表中的数据，使用str.format()方法格式化输出如图所示的格式。
    weather1 = ["2021年11月26日", "天气预报:晴", "20℃~7℃", "微风转西风3~4级"]
    weather2 = [["06:00", "晴", "10℃", "微风"],
                ["08:00", "晴", "13℃", "微风"],
                ["12:00", "晴", "19℃", "微风"],
                ["16:00", "睛", "18℃", "西风3~4级"],
                ["20:00", "晴", "15℃", "西风3~~4级"],
                ["00:00", "晴", "12℃", "微风"],
                ["04:00", "晴", "9℃", "微风"]]
    for i in weather1:
        print(i, end="\t")
    print()
    for i in weather2:
        print("时间：{0[0]} 天气：{0[1]} 温度：{0[2]} 风力：{0[3]}".format(i))

    # 6. 将日期中的汉字转化为阿拉伯数字，如“二零二一年一一月二陆日”转化为“2021年11月26日”。
    date_str = "二零二一年一一月二陆日"
    # 利用maketrans方法将汉字转化为阿拉伯数字
    t = str.maketrans('零一二三四五陆七八九', '0123456789')
    print(date_str.translate(t))

    # 7.对b'\xe6\x88\x91\xe7\x88\xb1\xe4\xb8\xad\xe5\x9b\xbd\xef\xbc\x8c\xe6\x88\x91\xe7\x88\xb1\xe5\xb7\x9d\xe4\xbf\xa1'字节串使用utf8界面，还原出字符串。
    str_bytes = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xb8\xad\xe5\x9b\xbd\xef\xbc\x8c\xe6\x88\x91\xe7\x88\xb1\xe5\xb7\x9d\xe4\xbf\xa1'
    print(str_bytes.decode('utf8'))

    # 8. (简答题)假设有一段英文，求长度为4的单词个数。
    # str1 = "I'm not afraid that if I try hard,\
    # I'm only afraid that those who are more successful than me will work harder than me."
    str1 = "I'm not afraid that if I try hard, I'm only afraid that those who are more successful than me will work harder than me."
    str1 = str1.replace(",", "").replace(".", "")
    new_list = []
    for i in str1.split():
        if len(i) == 4:
            new_list.append(i)
    print(len(new_list))