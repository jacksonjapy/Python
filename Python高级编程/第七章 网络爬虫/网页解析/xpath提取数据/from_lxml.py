from lxml import html

if __name__ == '__main__':
    html_path = r"./test.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    html_element = html.fromstring(html_content)    # 将字符串转换为Element(HTML)对象

    # 1.提取标题
    title_information = html_element.xpath("/html/head/title/text()")  # 绝对路径
    print(title_information[0])
    print("-" * 11)
    # 2.提取有用和无用的信息
    useful = html_element.xpath("//div[@class='useful']/ul/li[@class='info']/text()")
    useless = html_element.xpath("//div[@class='useless']/ul/li[@class='info']/text()")
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
    fault_informations = html_element.xpath("//div[position() >= 3 and position() <= 5]/text()")
    for fault in fault_informations:
        print(fault)
    print("-" * 11)
    # 5.
    html_element = html_element.xpath("//div[@id='test3']")[0]
    animal = html_element.xpath("string(.)")
    animal = str(animal).replace("\n", "").replace("\t", "")
    print(animal)
