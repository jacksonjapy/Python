import gmpy2

p = 473398607161
q = 4511491
e = 17

n = p * q
phi = (p-1) * (q-1)

d = gmpy2.invert(e, phi)
print(f'd = {d}')
