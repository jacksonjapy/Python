from requests import post

if __name__ == '__main__':
    url = "https://fanyi.baidu.com/sug"
    data = {
        "kw": "made in China"
    }
    response = post(url, data=data)
    result = response.json()
    print(result)
