from requests import get
from json import loads

if __name__ == '__main__':
    url = "https://www.httpbin.org/get"
    params = {"name": "张三", "age": 18}
    result = get(url, params=params)
    status_code = result.status_code    # 状态码提取
    if status_code != 200:
        print("请求失败")
        exit(1)
    r = result.text
    print(result.encoding)
    if result.json() == loads(result.content):   # 或者使用json模块的loads方法
       print(result.json())
