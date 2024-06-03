from requests import get
from lxml import html
from csv import DictWriter


def request_page(page_url):
    response = get(page_url)
    if response.status_code != 200:
        print("请求失败")
        return False
    else:
        return response.text


if __name__ == '__main__':
    main_url = "https://zjc.scitc.com.cn/"
    url = "https://zjc.scitc.com.cn/pagelist-6154.html"
    response = request_page(url)
    if not response:
        print("请求失败")
        exit(1)

    html_element = html.fromstring(response)  # 将结果转换为HTML对象
    max_page = "//span[@class='default_pgTotalPage']/text()"
    if max_page:
        max_page = int(html_element.xpath(max_page)[0])  # 获取最大页数
    else:
        print("获取最大页数失败")
        exit(1)

    for i in range(1, max_page + 1):
        print(f"正在爬取第{i}页")
        if i >= 2:  # 跳过第一页
            url = f"https://zjc.scitc.com.cn/pagelist-6154.html?pageye={i}"  # &pageSize=3
            re = request_page(url)
            if not re:
                print("请求失败")
                exit(1)
            html_element = html.fromstring(re)  # 将结果转换为HTML对象

        title = html_element.xpath("//div[2]/div[2]/div[2]/ul/li/a/h5/text()")
        title_url = html_element.xpath("//div[2]/div[2]/div[2]/ul/li/a/@href")

        if len(title) == len(title_url):
            pass
        else:
            print("获取标题和链接失败")
            exit(1)

        with open("result.csv", "a+", encoding="utf-8", newline="") as f:
            writer = DictWriter(f, fieldnames=["title", "url"])
            if i == 1:
                writer.writeheader()

            for index, name in enumerate(title):
                if str(title_url[index]).startswith("http"):
                    data = {"title": name, "url": title_url[index]}
                else:
                    data = {"title": name, "url": main_url + title_url[index]}
                writer.writerow(data)
