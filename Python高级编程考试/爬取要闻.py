from lxml.html import fromstring
from requests import get
from csv import DictWriter


def request_page(page_url):
    response = get(page_url)
    if response.status_code != 200:
        print("请求失败")
        return False
    else:
        return response.text


if __name__ == '__main__':
    main_url = "https://www.scitc.com.cn/"
    url = "https://www.scitc.com.cn/pagelist-6317.html"
    current_page = 1
    max_spider_page = 20
    title_xpath = "//ul[@class='list']/li[1]/a/text()"
    url_xpath = "//ul[@class='list']/li[1]/a/@href"

    for i in range(1, max_spider_page + 1):
        print(f"正在爬取第{i}页")
        url = f"https://www.scitc.com.cn/pagelist-6317.html?pageye={i}"
        re = request_page(url)
        # 判断请求是否成功
        if not re:
            print("请求失败")
            exit(1)

        html_element = fromstring(re)  # 将结果转换为HTML对象

        title = html_element.xpath(title_xpath)
        title_url = html_element.xpath(url_xpath)
        # 判断数据是否正确
        if len(title) == len(title_url):
            pass
        else:
            print("获取标题和链接失败")
            exit(1)
        for i in title:
            for j in title_url:
                print(i, j)
        # 写入数据
        with open("result.csv", "a+", encoding="utf-8", newline="") as f:
            writer = DictWriter(f, fieldnames=["index", "title", "url"])
            if i == 1:
                writer.writeheader()

            for index, name in enumerate(title):
                if "网络与通信学院" in name:
                    if str(title_url[index]).startswith("http"):
                        data = {"index": index + 1, "title": name, "url": title_url[index]}
                    else:
                        data = {"index": index + 1, "title": name, "url": main_url + title_url[index]}
                    writer.writerow(data)
