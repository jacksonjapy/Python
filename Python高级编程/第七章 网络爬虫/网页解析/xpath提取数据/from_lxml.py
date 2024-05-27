from lxml import html

if __name__ == '__main__':
    html_path = r"./test.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    html_element = html.fromstring(html_content)    # 将字符串转换为Element(HTML)对象
    useful = html_element.xpath("//div[@class='useful']/ul/li[@class='info']/text()")
    useless = html_element.xpath("//div[@class='useless']/ul/li[@class='info']/text()")
    # information = html_element.xpath("/html/head/title/text()")  # 绝对路径
    for yes in useful:
        print(yes)
    print("-" * 11)
    for no in useless:
        print(no)
