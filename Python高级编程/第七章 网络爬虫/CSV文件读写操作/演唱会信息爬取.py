from csv import DictWriter
from requests import Session

if __name__ == '__main__':
    url = "https://www.damai.cn/"
    current_page = 1
    info = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Cookie": "cna=m/rRHluqFE0CAT2d830d/9Tu; XSRF-TOKEN=4951673f-7e2f-4038-ad0a-57f81b308e73; destCity=%u6210%u90FD; tfstk=fnKmM0xWyy21Dlwti3jj45nXyr3RhSs16CEO6GCZz_57DE3fW12GZBkfkqTvr1AlNoLxlNCgI_A4XZKMClXwQCMf6xgJhKs1bXhK9DpXh_uCjh-00gyyFOVVQicMg6s1bXh8yl7jxGOK56MmjLklBOVV3C5V4u55KlSNgNPzz95P_GSw_g5PKt44brrqFcENth-W4veXF4YFK5KcnZfgX_qMu3Edk6JVZllejtV1TK5ubl5XBwmMLCc0At-GnU-Nl4GDnU82MTOixbjvJpK18nPrHt8HBHbdz7Uk1iXMdgtE9PQJSK-NrUiUstTwHhYwev4CdURXcFj3QmJlmsbFhamUjB7NKpsWYXUOyFv2baYSTyCeVL8pSIh7bsLHUQbp27EdDeppfw-4igkLzy7YQl6rB3z_5ZW5E6w-dPrULiiG7YDuRq_VFthKEY4_UZW5ECkoEywRuT6Az; isg=BLa22MNQzF-srrguXJTaXgvqB-W41_oRD1LRhiCeOxkvY1X9iGWEIbBRfz8PS_Ip",
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
