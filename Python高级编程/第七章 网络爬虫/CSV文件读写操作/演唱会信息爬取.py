from csv import DictWriter
from requests import Session
from time import sleep

if __name__ == '__main__':
    current_page = 1
    url = f"https://search.damai.cn/searchajax.html?keyword=&cty=&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&sctl=&tsg=0&st=&et=&order=1&pageSize=30&currPage={current_page}&tn="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Cookie": "cna=m/rRHluqFE0CAT2d830d/9Tu; destCity=%u5168%u56FD; xlly_s=1; XSRF-TOKEN=d3ce40e7-ba6e-48ad-b4f2-2940f3f55815; isg=BLu7TQwHWaq70GU9kTOPPa4FSpYlEM8Sim1sNa14l7rRDNvuNeBfYtlOIqxCLCcK; tfstk=f5nmT5mSywX_OTX9i0qX5kHbd_T8csZ_6fIT6lFwz7P5DqLbW5XgZXJbkEgxr5cuNi3vlPFGI7cVXrniCG2ZQf9b6KT-hxZ_bBdp9HHjhUemzKR8bdkz4W8KVHKKhxWY3pHyvd6glHNT_lz4u_PzNRw4QfPqUL2aBs7N0fkyERNzQRS4uzPzLR54Qx2cbWmZV0R0PbAApPUsq-42yxPPb8iunrVE3mjNb9w0oWk4ZBCojUzngPm6Kgcoj54TOr6eSukIyjyuxH1464Hnj2kXKZVKuvanJzCRyXcxw04-oF6ba4DrJ8o2paN-zRDQq09AP8gLQuoq-OSZEo0Y88lViGliMbnuyqY1h7uoU2UrPIb7gmwZ1yi9OiNqQviIJkxCg53-Kc0G4vQP8rBNf8Jt4N__u8wuOTpC7MWUch4wELbBlry7HBpkEN6zu8wo_LvlRTU4F-UP.",
        "Referer": "https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.591b23e1Dxm7wS&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty="
    }
    print(f"正在爬取第{current_page}页")
    session = Session()
    r = session.get(url=url, headers=headers)

    if r.status_code != 200:
        print("请求失败")
        exit(1)
    save_path = f"演唱会信息.csv"
    with open(save_path, "w", encoding="utf-8", newline="") as file:
        fieldnames = ("演唱会名称", "艺人", "地点", "时间", "票价", "链接")
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        result = r.json()
        if "pageData" in result:
            total = result["pageData"]["totalPage"]  # 提取总页面数量
            total_result = result["pageData"]["totalResults"]   # 提取数据总条数

            current_result = 0  # 已经爬取的数据条数
            for current_page in range(1, total+1):
                if current_page >= 2:
                    print(f"正在爬取第{current_page}页")
                    target_url = f"https://search.damai.cn/searchajax.html?keyword=&cty=&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&sctl=&tsg=0&st=&et=&order=1&pageSize=30&currPage={current_page}&tn="
                    r = session.get(url=target_url, headers=headers)
                    if r.status_code != 200:
                        print("请求失败")
                        exit(1)
                    result = r.json()
                # 提取数据（演唱会名称，艺人，地点，时间，票价，链接）
                if result_data := result["pageData"]["resultData"]:
                    for info in result_data:
                        name = info["name"]
                        actor = info["actors"]
                        ip_address = info["venuecity"]
                        showtime = info["showtime"]
                        price = info["price_str"]
                        url = f"https://detail.damai.com/item.htm?id={info['projectid']}&clicktitle={name}"
                        current_result += 1
                        writer.writerow({
                            "演唱会名称": name,
                            "艺人": actor,
                            "地点": ip_address,
                            "时间": showtime,
                            "票价": price,
                            "链接": url
                        })
                sleep(0.5)
