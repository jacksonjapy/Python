from csv import DictWriter
from requests import Session

if __name__ == '__main__':
    url = "https://www.damai.cn/"
    current_page = 1
    info = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Cookie": "cna=m/rRHluqFE0CAT2d830d/9Tu; destCity=%u5168%u56FD; xlly_s=1; XSRF-TOKEN=dda8f4f3-eb8a-44ff-9ce6-f5fa0cfec34a; isg=BOjoR2q1Guwf9jZEXpLshGnUud_6EUwbbTzfbKIZNGNW_YhnSiEcq34_8ZUNVgTz; tfstk=fLbkrKbfDccQoBcLEZY7AFYCaBrANYTBp93ppepU0KJjygEWvpcHnOPW2usRmpXDh4I8VHpntKXrJ3QhO2AFT9NWp7ZAN_TB8ReTBPC5NhoJSHyv8W52udrOlPUON_8B8ReTWWMH5k-kLe-y4x-2hBOyT9-EgSAe9YoEz954iB92Lxej8dbFlZyk0TSHVxDcoQyBQ_vDGI_DZ3va5K0FwZAkqd5PPzasUCjGohIzauRM-K15k32iQe1Aj9jFe-geeGf2zKIz3V9VfL8RPeGE4nQATwLVM8ukEiW5Lnj7E4pyxaIH2GwifpKeth8emXuFi_plLIYZEVxAk67puserrLjVFw8R75nBGHSAPh_834YNf_LRYTej8LIGgEjrpmow2XuBgWQqADtyGIvsM5iE7f87-HP0icZW4IO8BSVmAj-yGIXUiSmsM3RXwn5..",
        "Referer": "https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.591b23e1Dxm7wS&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty="
    }
    session = Session()
    r = session.get(url=url, headers=info)

    if r.status_code != 200:
        print("请求失败")
        exit(1)

    result = r.json()
    if "page" in result:
        total = result["pageData"]["totalPage"]

        for current_page in range(1, total+1):
            if current_page >= 2:
                target_url = f"https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.591b23e1V3Syga&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=%E6%88%90%E9%83%BD&page={current_page}"
                r = session.get(url=target_url, headers=info)
                if r.status_code != 200:
                    print("请求失败")
                    exit(1)
                result = r.json()
        # 提取数据（演唱会名称，艺人，地点，时间，票价，链接）
        if "resultData" in result["pageData"]:
            info = result["pageData"]["resultData"]
            print(info)
            name = info[0]["actors"]
            actor = info[0]["description"]
            ip_address = info[0]["name"]
            time = info[0]["showtime"]
            price = info[0]["price_str"]
            url = f"https://detail.damai.com/item.htm?id={info[0]['projectid']}&clicktitle={name}"
            if current_page >= 1:
                exit(1)
