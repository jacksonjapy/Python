from requests import Session
from lxml.html import fromstring

if __name__ == '__main__':
    url = 'https://mooc1-1.chaoxing.com/mooc-ans/visit/courselistdata'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "Cookie": "lv=4; fid=3012; xxtenc=a580cc8736e8f3106c722802b50214cf; _uid=114143897; uf=94ffe74515793f3650e40adf303dc5cf9d2d8d7cae0cd990a5f176ee996a3a58e9f4b96aceaa03eb0c1ea2177a015a46913b662843f1f4ad6d92e371d7fdf644aef179cf7a5fa13a22d37f0ce2a6151deea6be31981211d285aae28325dbd0ce85d4926bd03a87a6; _d=1718096377241; UID=114143897; vc=4B150AAF9BFFCB828E2963B8B71CB34B; vc2=D1B537BDB2FF4AEC5CB59A9E71103366; vc3=VO970J4jLjSf2OQHyucYEXxh9BcoLiRuzLtizirqyjHFCDwv5Rq3wUR3XJ77rOH3G%2B7%2FuY51Zfe2wNG2zJMcBMGNs%2BrtyISn8g2X8k7P5ymfvAC3ZSV%2Be8BlUZcZj8qbgdRtx4AtWVpoqMDsCAh5K1zqqScAjva9d1mmPYs0nXE%3Db8f6f6ff77c767c8989b13b72981206e; cx_p_token=62e72d431960171480951ba5327b7a0b; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxMTQxNDM4OTciLCJsb2dpblRpbWUiOjE3MTgwOTYzNzcyNDIsImV4cCI6MTcxODcwMTE3N30.cSpPzgNGGKGG8u92Vv-H9U4CFunoWKW6R2X46nZ-8zs; DSSTASH_LOG=C_38-UN_1909-US_114143897-T_1718096377242; tl=1; source=""; spaceFid=3012; spaceRoleId=""; k8s=1718172521.064.1312.217425; jrose=4E2044E16A98F69FC4BC3B7456F0F5B7.mooc-3926409564-x0vdz; route=6c7e83002ce2cc0e78a680d806381539"
    }
    data = {
            "courseType": "1",
            "courseFolderId": "0",
            "baseEducation": "0",
            "superstarClass": "",
            "courseFolderSize": "0"
    }
    sess = Session()
    result = sess.post(url=url, headers=headers, data=data)
    if result.status_code != 200:
        print('请求失败')
        exit(1)

    r = result.text
    html_element = fromstring(r)
    course_xpath = "//span[@class='course-name overHidden2']/text()"
    course_url = "//a[@class='color1']/@href"
    course_name = html_element.xpath(course_xpath)
    course_url = html_element.xpath(course_url)

    if len(course_name) != len(course_url):
        print('数据异常')
        exit(1)

    print(f"共有{len(course_name)}门课！")

    for index, c_name in enumerate(course_name):
        c_name = str(c_name).strip()
        c_url = course_url[index]

        if "https" not in course_url[index]:
            c_url = "https://mooc2-ans.chaoxing.com"+course_url[index]
            print(c_name, c_url)
        else:
            print(c_name, c_url)
