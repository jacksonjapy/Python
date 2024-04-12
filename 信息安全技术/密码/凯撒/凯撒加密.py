if __name__ == '__main__':
    # 加密
    # def encrypt(message, key):
    #     encrypted_char = ''
    #     for char in message:
    #         if char.isalpha():
    #             if char.isupper():
    #                 encrypted_char += chr((ord(char) + key - ord('A')) % 26 + ord('A'))
    #             else:
    #                 encrypted_char += chr((ord(char) + key - ord('a')) % 26 + ord('a'))
    #     return encrypted_char
    # message = input('请输入要加密的消息：')
    # key = int(input('请输入加密的密钥：'))
    # encrypted_message = encrypt(message, key)
    # print('加密后的消息为：', encrypted_message)
    def encrypto(s, k):
        result = ''
        for i in s:
            if i.isupper():
                result += chr((ord(i) + k - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(i) + k - ord('a')) % 26 + ord('a'))
        return result


    def decrypto(s, k):
        result = ''
        for i in s:
            if i.isupper():
                result += chr((ord(i) - k - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(i) - k - ord('a')) % 26 + ord('a'))
        return result


    if __name__ == '__main__':
        while True:
            choose = input('请输入选择\n1.加密\n2.解密\n3.退出\n请输入选择：')
            if choose == '1':
                s = input('请输入加密明文:')
                k = int(input('请输入位移长度:'))
                print('加密结果为:{}'.format(encrypto(s, k)))
            elif choose == '2':
                s = input('请输入加密密文:')
                for i in range(26):
                    print('当k={}时，结果为:{}'.format(i, decrypto(s, i)))
            else:
                break
