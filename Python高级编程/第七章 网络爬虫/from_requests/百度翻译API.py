import requests
import hashlib
import base64
import time

# 百度翻译API密钥
APPID = '20240521002057705'
API_KEY = 'Qeuuz_a8f00jvOTricB8'

# 有效的语言代码列表（示例）
valid_langs = {'zh', 'en', 'ja', 'ko', 'fr', 'es', 'de', 'pt', 'ru', 'it', 'nl', 'pl', 'vi', 'ar', 'tr', 'th', 'el',
               'bg', 'ca', 'cs', 'da', 'et', 'fa', 'fi', 'he', 'hi', 'hr', 'hu', 'lt', 'lv', 'no', 'ro', 'sk', 'sl',
               'sr', 'sv', 'uk', 'zh-CN', 'zh-TW', 'zh-HK'}


# 获取用户输入的源语言和目标语言，并进行验证
def get_user_langs():
    while True:
        from_lang = input("请输入源语言代码（如zh表示中文，en表示英文）: ").strip().lower()
        if from_lang in valid_langs:
            break
        print("无效的源语言代码，请重新输入。")

    while True:
        to_lang = input("请输入目标语言代码（如zh表示中文，en表示英文）: ").strip().lower()
        if to_lang in valid_langs:
            break
        print("无效的目标语言代码，请重新输入。")
    return from_lang, to_lang


# 获取用户输入的翻译内容
def get_user_query():
    while True:
        query = input("请输入要翻译的文本: ")
        if query.strip():  # 确保非空输入
            break
        print("请输入有效的文本内容。")
    return query


# 计算签名
def get_sign(api_key, query):
    m2 = hashlib.md5()
    string_to_sign = f"{api_key}{query}{API_KEY}".encode('utf-8')
    m2.update(string_to_sign)
    return base64.b64encode(m2.digest()).decode()


# 获取签名和翻译内容
sign = get_sign(APPID, get_user_query())
query = get_user_query()  # 注意这里再次调用了get_user_query()来获取翻译内容，你可能想优化这一点

# 构造请求的URL和参数
url = 'http://api.fanyi.baidu.com/api/trans/v2'
from_lang, to_lang = get_user_langs()
params = {
    'q': query,
    'from': from_lang,
    'to': to_lang,
    'appid': APPID,
    # 注意：百度翻译免费接口可能不需要salt字段，或者salt字段的用途与VIP接口不同
    'salt': int(time.time()),  # 如果API文档说明需要这个字段，则取消注释并可能需要进行其他处理
    'sign': sign,
}

# 发送GET请求
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}  # 添加User-Agent头以避免被识别为爬虫
response = requests.get(url, params=params, headers=headers)

# 解析返回的结果
result = response.json()

# 输出翻译结果
if 'trans_result' in result and result['trans_result']:
    translation = result['trans_result'][0]['dst']
    print(f"翻译结果: {translation}")
else:
    print('翻译失败:', result.get('error_msg', '未知错误'))
