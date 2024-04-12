from Crypto.Util.number import inverse, long_to_bytes

# 假设已知的RSA参数
e = 3  # 公钥指数
N = [  # 模数列表
    # N1,
    # N2,
    # N3,
]
c = [  # 密文列表
    # c1,
    # c2,
    # c3,
]

# 使用中国剩余定理解决Håstad's Broadcast Attack
def chinese_remainder_theorem(items):
    # items: [(c1, N1), (c2, N2), (c3, N3)]
    N = 1
    for a, n in items:
        N *= n
    result = 0
    for a, n in items:
        m = N // n
        d, r, s = extended_gcd(n, m)
        if d != 1:
            raise "Input not pairwise co-prime"
        result += a * s * m
    return result % N, N

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

# 解密过程
try:
    M, _ = chinese_remainder_theorem(list(zip(c, N)))
    m = int(M ** (1/e))  # 假设e是3
    flag = long_to_bytes(m)
    print("Flag:", flag.decode())
except Exception as ex:
    print("Error:", ex)
