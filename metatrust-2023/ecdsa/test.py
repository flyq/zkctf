from sympy.core.numbers import igcdex


def div_mod(n, m, p):
    """
    Finds a nonnegative integer x < p such that (m * x) % p == n.
    """
    a, b, c = igcdex(m, p)

    print("a", a)
    assert c == 1
    return (n * a) % p


# Returns (x / y) % P
def bigint_div_mod(x, y, P):
    res = div_mod(x, y, P)
    return res


msg_hash = 0xCA1AD489AB60EA581E6C119CC39D94DDBFC5FAA0E178A23CA66202C8C2A72277
s = 0x1878DBC4684DE3A63A5975325B467CDBA846B24D949322016FE4C8FD2C0862A1
SN = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
r = 0x22C2921ACF3A393A0BBAF1F68EE7E02F8385FF60CA67C41A1DE3CFF3FDAA1A74

u1 = bigint_div_mod(msg_hash, s, SN)

print(u1)

u2 = bigint_div_mod(r, s, SN)

print(u2)
