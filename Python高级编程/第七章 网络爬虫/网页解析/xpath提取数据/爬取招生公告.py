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
    main_url = "https://zjc.scitc.com.cn/"
    url = "https://zjc.scitc.com.cn/pagelist-6154.html"
    response = request_page(url)
    if not response:
        print("请求失败")
        exit(1)

    html_element = html.fromstring(response)
    max_page = "//span[@class='default_pgTotalPage']/text()"
    if max_page:
        max_page = int(html_element.xpath(max_page)[0])
    title_dict = dict()
    url_dict = dict()
    for i in range(1, max_page + 1):
        print(f"正在爬取第{i}页")
        if i >= 2:  # 跳过第一页
            url = f"https://zjc.scitc.com.cn/pagelist-6154.html?pageye={i}&pageSize=3"
            re = request_page(url)
            if not re:
                exit(1)
            html_element = html.fromstring(re)

        title = html_element.xpath("//div[2]/div[2]/div[2]/ul/li/a/h5/text()")
        title_url = html_element.xpath("//div[2]/div[2]/div[2]/ul/li/a/@href")
        title_dict[str(i)] = title
        url_dict[str(i)] = title_url

    with open("data.txt", "w", encoding="utf-8") as f:
        for i in range(1, max_page + 1):
            for j in range(len(title_dict[str(i)])):
                if "http" not in url_dict[str(i)][j]:
                    f.write(f"{title_dict[str(i)][j]} {main_url + url_dict[str(i)][j]}\n")
                else:
                    f.write(f"{title_dict[str(i)][j]} {url_dict[str(i)][j]}\n")
