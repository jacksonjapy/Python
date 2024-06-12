from requests import Session

if __name__ == '__main__':
    target_url = "https://passport2.chaoxing.com/fanyalogin"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": "fid=3012; JSESSIONID=F38792662B8ED66466C1CE9033C5D799; route=52ffa9af7a380e114204ed76732d509c; source=""; retainlogin=1"
    }
    data = {
        "fid": "-1",
        "uname": "1TwSugLGH5kBhWNRys18QdQ==",
        "password": "+KahGBNxTWFMyJzOpyFzOw==",
        "refer": "https%3A%2F%2Fi.chaoxing.com",
        "t": "true",
        "forbidotherlogin": "0",
        "validate": "",
        "doubleFactorLogin": "0",
        "independentId": "0",
        "independentNameId": "0"
    }
    sess = Session()
    response = sess.post(url=target_url, headers=headers, data=data)
    if response.status_code != 200:
        print("登录失败")
        exit(1)

    login_result = response.json()
    if login_result["status"]:
        print("登录成功")
        print(login_result)
    elif not login_result["status"]:
        print("登录失败")
        print(login_result)
