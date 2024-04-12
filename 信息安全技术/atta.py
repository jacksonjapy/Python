"""
By Jackson Ja
"""
import sympy
import gmpy2

# import crypt

if __name__ == "__main__":
    c = 0x7a7e031f14f6b6c3292d11a41161d2491ce8bcdc67ef1baa9e
    e = 0x872a335
    k1 = 1285367317452089980789441829580397855321901891350429414413655782431779727560841427444135440068248152908241981758331600586
    k2 = 1109691832903289208389283296592510864729403914873734836011311325874120780079555500202475594
    # q + q*p^3 - k1 = 0
    # qp + q *p^2 - k2 = 0
    p, q = sympy.symbols('p q')
    solve_value = sympy.solve([q + q * p ** 3 - k1, q * p + q * p ** 2 - k2], [p, q])
    p = int(solve_value[1][0])
    q = int(solve_value[1][1])
    n = p * q
    d = gmpy2.invert(e, (p - 1) * (q - 1))
    m = gmpy2.powmod(c, d, n)
    print(bytes.fromhex(hex(m)[2:]))
