from requests import get

if __name__ == '__main__':
    image_url = "https://logohistory.net/wp-content/uploads/2023/06/Python-Emblem.png"
    result = get(image_url)
    image_path = input(r"请输入保存图片的路径:")+"/logo.png"
    print(image_path)
    with open(image_path, "wb") as f:   # 以二进制写的模式打开文件
        f.write(result.content)
