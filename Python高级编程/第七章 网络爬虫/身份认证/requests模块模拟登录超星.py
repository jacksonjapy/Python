from requests import Session
from lxml.html import fromstring

if __name__ == '__main__':
    your_name = input("请输入你的真实姓名：")
    target_url = "https://passport2.chaoxing.com/fanyalogin"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": "fid=3012; JSESSIONID=F38792662B8ED66466C1CE9033C5D799; route=52ffa9af7a380e114204ed76732d509c; source=""; retainlogin=1"
    }
    data = {
        "fid": "-1",
        "uname": "TwSugLGH5kBhWNRys18QdQ==",
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
    if ("url" in login_result) or ("msg2" in login_result) and ("status" in login_result):
        if login_result["status"]:
            print("登录成功")
        elif not login_result["status"]:
            print("登录失败")

        success_url = "https://i.mooc.chaoxing.com/"
        headers["Cookie"] = "fid=3012; jrose=7B67B09CC218E47210EACBDD186E245A.ans; spaceFidEnc=3AFBB0391D30E83E973E45D2E4C9917E; source=""; lv=4; _uid=114143897; uf=94ffe74515793f3650e40adf303dc5cf9d2d8d7cae0cd990a5f176ee996a3a58732534f1ee2d5ee7afeb1495e1d621d1913b662843f1f4ad6d92e371d7fdf644aef179cf7a5fa13a22d37f0ce2a6151deea6be31981211d2b51ee50fde29ad09ae1af07f97c7e6ea; _d=1718173761111; UID=114143897; vc=4B150AAF9BFFCB828E2963B8B71CB34B; vc2=DE157B6D400FE4CB7A1C6AAFB130E616; vc3=USGPtk6%2FU6oxeVrM9moge2kkgE1Lhs2yFQb9EEInS1c9Rzg8S%2FttMlUxajRYoWrLoD6qdJuWdEi1CCdhs2VEFZfAsdNFKhM4yTgLdSTS8LIqs6CaSB9iPT4jIp52gC2Y1heoTqAPpMJnpZ8EZWMDPSEowQ76aCoJsq5pP%2BE%2Fw%2FE%3Dd97483aa3fc35b499a14468c69cba1d9; cx_p_token=b4d216e12a3d69923568ce5c2006d595; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxMTQxNDM4OTciLCJsb2dpblRpbWUiOjE3MTgxNzM3NjExMTMsImV4cCI6MTcxODc3ODU2MX0.i5yWCwi15T_Ij659NqSL0V8LxT58zgE_vPrFw6fDn14; xxtenc=a580cc8736e8f3106c722802b50214cf; DSSTASH_LOG=C_38-UN_1909-US_114143897-T_1718173761113"
        success_response = sess.get(url=success_url, headers=headers)
        if success_response.status_code != 200:
            print("获取成功页面失败")
            exit(1)
        elif success_response.status_code == 200:
            username_xpath = '//p[@class="personalName"]/@title'
            html_element = fromstring(success_response.text)
            user_name = html_element.xpath(username_xpath)
            if your_name in user_name:
                print(f"{your_name} \033[32m用户登录成功\033[0m ")
            elif your_name not in user_name:
                print(f"{your_name} \033[31m用户登录失败\033[0m ")
