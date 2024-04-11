if __name__ == '__main__':
    s = "学Python了:@张三@李四@王五@赵六"
    print(s.count('@'))
    print(s.find('张三'))
    urls = ["https://www.icann.org",
            "https://www.heroku.com",
            "https://edu.gcfglobal.org",
            "https://www.gimp.org",
            "https://betanews.com",
            "https://www.nhl.com/oilers",
            "https://www.ecb.co.uk",
            "https://www.anantara.com.cn"]
    # 取出org结尾的url
    for url in urls:
        if url.endswith('org'):
            print(url)

    s = '这一伙人干着非法买卖，行为野蛮，还喜欢使用暴力！'
    words = ['非法', '暴力', '野蛮']
    #将words中的内容替换成**
    for word in words:
        s = s.replace(word, '**')
    print(s)