from requests import Session

if __name__ == '__main__':
    keep_session = Session()  # 创建会话对象
    url = 'http://httpbin.org/cookies/set?cookie=123456789'
    params = {'Cookie_value': '12345'}
    for i in range(0, 2):
        print('第%d次请求' % (i + 1))
        response = keep_session.get(url, params=params)
        print(response.json())
