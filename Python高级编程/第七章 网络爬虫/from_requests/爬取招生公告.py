from requests import get
from lxml import html


def request_page(page_url):
    response = get(page_url)
    if response.status_code != 200:
        print("请求失败")
        return False
    else:
        return response.text


if __name__ == '__main__':
    url = "https://zjc.scitc.com.cn/pagelist-6154.html"
    response = request_page(url)
    if not response:
        exit(1)

    html_element = html.fromstring(response)
    max_page = "//span[@class='default_pgTotalPage']/text()"
    if max_page:
        max_page = int(html_element.xpath(max_page)[0])
    for i in range(1, max_page + 1):
        print(f"正在爬取第{i}页")
        if i >= 2:  # 跳过第一页
            url += f"?pageye={i}"
            re = request_page(url)
            if not re:
                exit(1)
            html_element = html.fromstring(re)

    title = html_element.xpath("//div[2]/div[2]/div[2]/ul/li[1]/a/h5/text()")
    title_url = html_element.xpath("//div[2]/div[2]/div[2]/ul/li/a/@href")
    print(title, "\n", title_url)
