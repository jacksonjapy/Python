from requests import post

if __name__ == '__main__':
    url = "https://fanyi.baidu.com/sug"
    while True:
        source = input("请输入要翻译的文本：")
        data = {"kw": source}
        response = post(url, data=data)
        if response.status_code == 200:
            result = response.json()
            if "data" in result:
                for item in result["data"]:
                    print(f"原文：{item['k']}\n译文：{item['v']}")
                break
        else:
            print("请求失败")
            break
