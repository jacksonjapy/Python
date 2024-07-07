def decrypt(c, key1, key2):
    key1 = key1.encode("utf-8")
    key2 = key2.encode("utf-8")
    c = c.encode("utf-8")
    key1 = key1[::-1]
    key2 = key2[::-1]
    c = c[::-1]
    key1 = key1.decode("utf-8")
    key2 = key2.decode("utf-8")
    c = c.decode("utf-8")


if __name__ == '__main__':
    key1 = "security"
    key2 = "information"
    c = "zhnjinhoopcfcuktlj"
    # 解密四方密码
    print(decrypt(c, key1, key2))
