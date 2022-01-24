def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m

# print(gcd(540, 24458732646))

def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)

# print(gcd2(540, 24458732646))


def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m

print(gcd3(540, 24458732646))