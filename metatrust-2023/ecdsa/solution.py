#!/usr/bin/python3
from miniecdsa import *

x1 = 0x53B907251BC1CEB7AB0EB41323AFB7126600FE4CB2A9A2E8A797127508F97009
y1 = 0xC7B390484E2BAAE92DF41F50E537E57185CB18017650A6D3220A42A97727217D
P1 = EPoint(x1, y1)

pm3 = 0xD935BB512B4F5E4BCB07F2BE42EE5A54804379008B86B9C6C98FD605CCA64F55

pm1_P1 = mult(P1, pm1)
pm2_P1 = mult(P1, pm2)
pm3_P1 = mult(P1, pm3)

s1s2 = bigint_mul_mod(ps1, ps2, SN)
pm1_sub_pm2 = bigint_sub_mod(pm1_P1.x, pm2_P1.x, SN)

ps1ps2_times__x1_sub_x2 = bigint_mul_mod(s1s2, pm1_sub_pm2, SN)

s2m1 = bigint_mul_mod(pm1, ps2, SN)
s1m2 = bigint_mul_mod(pm2, ps1, SN)
r1s2 = bigint_mul_mod(pr1, ps2, SN)
r2s1 = bigint_mul_mod(pr2, ps1, SN)

s1m2_sub_s2m1 = bigint_sub_mod(s1m2, s2m1, SN)

temp1 = bigint_add_mod(ps1ps2_times__x1_sub_x2, s1m2_sub_s2m1, SN)

# r1s2 - r2s1
temp2 = bigint_sub_mod(r1s2, r2s1, SN)

sk = bigint_div_mod(temp1, temp2, SN)
print("sk =", hex(sk))
print("pubkey=", hex(pubkey(sk).x), hex(pubkey(sk).y))

(pr3, ps3) = sign_ecdsa(sk, pm3)
print("pr3:", hex(pr3))
print("ps3:", hex(ps3))

print(verify_ctf(pr3, ps3))
