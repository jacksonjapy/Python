import gmpy2
import rsa

if __name__ == '__main__':
    n = 86934482296048119190666062003494800588905656017203025617216654058378322103517
    e = 65537
    p = 285960468890451637935629440372639283459
    q = 304008741604601924494328155975272418463
    d = gmpy2.invert(e, (p - 1) * (q - 1))
    key = rsa.PrivateKey(n, e, d, p, q)
    # print(key)
    path = r"/home/jackson/Downloads/flag.enc"
    with open(path, "rb") as f:
        file01 = f.read()
        print(rsa.decrypt(file01, key))
