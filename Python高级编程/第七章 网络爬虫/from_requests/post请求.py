from requests import post

if __name__ == '__main__':
    url = "https://httpbin.org/post"
    data = {"name": "张三", "age": 18, }
    response = post(url, data=data)
    result = response.json()
    print(result)
