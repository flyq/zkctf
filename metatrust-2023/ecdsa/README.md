# ECDSA

## problem description
> get your signature!
> 
> Alice intercepted the two signatures form Bob who used miniecdsa.py to sign his message.
> Can you help Alice to pass the solve function in Verify.sol?
>

According to miniecdsa.py, it provides the ECDSA functions on the curve secp256r1. And given two different signatures((`pr1`, `ps1`), (`pr2`, `ps2`)) generated by the same private key, it is requested to calculate the signature of the private key for the given message hash (`pm3`).

## solution description

### backgroud
**Elliptic Curve Cryptography**

the add:

![Alt text](./img/image.png)

the scalar multipulication:

$P = n \cdot G = \sum_1^n G$

it is a ECDLP.

**ECDSA Sign**
* choose a random $k$
* calculate the point $P = kG$, the $r = P.x$
* the $s = \frac{msg\_hash + r \cdot sk}{k}$
* $(r, s)$ is the signature


One disadvantage of the ECDSA algorithm is that cryptographically secure random numbers need to be used to generate k for each signature, which requires a high quality random source.

There are already some Deterministic Usage for ECDSA, such as [RFC6979](https://datatracker.ietf.org/doc/rfc6979/)

### solution
In this challenge, due to the wrong deterministic K algorithm, the private key can be calculated through any two legal signatures.

```py
def random(m, s):
    x1 = 0x53B907251BC1CEB7AB0EB41323AFB7126600FE4CB2A9A2E8A797127508F97009
    y1 = 0xC7B390484E2BAAE92DF41F50E537E57185CB18017650A6D3220A42A97727217D
    x2 = 0xACBC2999FB58C6E9015A12A4C5F3849E301649B2271EAAAF21906ED03CAFDF45
    y2 = 0x146AAC3F7F74047FD45CF0098FADEE5CD00F7F6871440387BA402F2390D7276F
    P1 = EPoint(x1, y1)
    P2 = EPoint(x2, y2)

    PM1 = mult(P1, m)
    PS1 = mult(P2, s)

    res = bigint_add_mod(PM1.x, PS1.x, SN)

    # print("random = (",hex(res),")")
    return res
```
* msg_hash: $m_i$
* signature: $(r_i, s_i)$
* private key: $sk$
* deterministic k: $k_i = [m_i \cdot P_1].x + [sk \cdot P_2].x$, and point $P_1$ and $P_2$ is on the same curve, and they are public. let $pm_i = [m_i \cdot P_1].x$ and $a = [sk \cdot P_2].x$, so $k_i = pm_i + a$, a is a unknow **constant** number.

$$\begin{align*}
&\Rightarrow
\left\{\begin{matrix}
s_1 = \frac{m_1 + r_1 \cdot sk}{pm_1 + a} 
\\ 
s_2 = \frac{m_2 + r_2 \cdot sk}{pm_2 + a} 
\end{matrix}\right.
\\
&\Rightarrow
\left\{\begin{matrix}
s_1(pm_1 + a) = m_1 + r_1 \cdot sk
\\ 
s_2(pm_2 + a) = m_2 + r_2 \cdot sk
\end{matrix}\right.
\end{align*}$$

Two unknowns and two linear equations can calculate $sk = \frac{s_1s_2(pm_1 - pm_2) + (m_2s_1 - m_1s_2)}{r_1s_2 - r_2s_1}$

## running

```sh
cd zkctf/

python3 metatrust-2023/ecdsa/solution.py
res_pm1 =  1
res_pm2 =  1
sk = 0x3b82478cddee8de342cb5dd31c8dcaf4b0bc6d51af35a147309c42f74a0481e5
pubkey= 0x209d386328994af4bbf0ff8bb6cdbb0e87e01e2118b1c12b94c555a1726129c6 0x76ac8f2fda3a921bd3dcc1d2f0741b91dcd18d053a67a4ece89761e64a0881b1
pr3: 0x8ca09723f24865bbc3fd194cc60cc95a77943ed5b38671887007072ba917a5ea
ps3: 0xb36a63f0329d0ad45be9bbdea6f62508a9add0d79c51c97adc11dfb720cad37a
1
```

## others
how to calculate $1/2P$?

For the elliptic curve group of order $n$, let $Q = 1/2 P$, because $\frac {n+1}{2} \cdot 2 \equiv 1 \mod n$, so $\frac{n+1}{2} \equiv \frac{1}{2} \mod n$, so $Q = \frac{n+1}{2} P$, we can calculate $\frac{n+1}{2}$  easily.

how to calculate $\sqrt{a} \mod n$?
```py
SP = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
# > F = GF(SP)
# > y_sqr2 = F.from_integer(0x55936ba5f40af4a80bc019b90a3afb30c1f5a5268d3cda04fc4dc4c86cae5c84)
# > y_sqr2.sqrt(extend=False, all=True)
# [16266993938295423052800445989939399534749345174288806400925877505453552280846,
# 99525095272060825709897000959468173995336798241001507794607753803413545573105]
```


## reference
* https://docs.google.com/presentation/d/1_Z-0bjIM15UaZjq6lpizZCV2azGn_zcz/edit#slide=id.p1