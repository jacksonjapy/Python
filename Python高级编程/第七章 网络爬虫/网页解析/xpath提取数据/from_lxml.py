from lxml import html

if __name__ == '__main__':
    html_path = r"./test.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    html_element = html.fromstring(html_content)    # 将字符串转换为Element(HTML)对象

    useful = html_element.xpath("//div[@class='useful']/ul/li[@class='info']/text()")
    useless = html_element.xpath("//div[@class='useless']/ul/li[@class='info']/text()")
    title_information = html_element.xpath("/html/head/title/text()")  # 绝对路径
    # 1.提取标题
    print(title_information[0])
    print("-" * 11)
    # 2.提取有用和无用的信息
    for sure in useful:
        print(sure)
    print("-" * 11)
    for no in useless:
        print(no)
    # 3.提取有用的信息
    for yes in useful:
        print(yes)
    print("-" * 11)
    # 4.提取id属性为"testfault", "test-1", "test-2"的信息
    fault_informations = (html_element.xpath("//div[@id='testfault']/text()"),
    html_element.xpath("//div[@id='test-1']/text()"),
    html_element.xpath("//div[@id='test-2']/text()"))
    for fault in fault_informations:
        print(fault[0])
    # 5.
    div = html_element.xpath("//div[@id='test3']/text()")
    span = html_element.xpath("//span[@id='tiger']/text()")
    ul = html_element.xpath("//span[@id='tiger']/ul/text()")
    li = html_element.xpath("//span[@id='tiger']/ul/li/text()")
    long = str(div[0]).strip()
    hu = str(span[0]).strip()
    zhu = str(ul[0]).strip()
    wu = str(li[0]).strip()
    tou = str(div[1]).strip()
    cow = str(span[1]).strip()
    animal = (long, hu, zhu, wu, cow, tou)
    for j in animal:
        print(j, end="")
