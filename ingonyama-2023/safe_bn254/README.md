# Safe bn254

## problem description
> doesn’t bn254 look safer now?
> 
> y^2=x^3+2023 if you are not afraid of generating curves and discrete logarithms, you could try looking for a flag in x, where res = x * curve_gen
> 
> The generators are given by (in affine coordinates)
> 
> curve_gen_x=14810849444223915365675197147935386463496555902363368947484943637353816116538 curve_gen_y=742647408428947575362456675910688304313089065515277648070767281175728054553
> 
> The result coordinates are res_x=5547094896230060345977898543873469282119259956812769264843946971664050560756 res_y=14961832535963026880436662513768132861653428490706468784706450723166120307238
> 
> you can use any language for finding the solution and convert the flag into text format
> 
> The prime modulus in GF(p) p=21888242871839275222246405745257275088696311157297823662689037894645226208583


## solution description
In layman's terms, this question is about how to calculate the private key based on the public key, that is, solving ECDLP. Of course, only incorrect curve parameters can be completed with existing computing power.

The ECDLP problem, generally regarded as computationally infeasible, hinges on the order of the subgroup of the elliptic curve. The curve should have a large prime order subgroup, as operations are conducted in this group. If the subgroup's order is small, the [Pohlig-Hellman algorithm](https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm) can be used to fragment the problem into smaller, solvable parts. These parts can then be pieced back together using the Chinese Remainder Theorem (CRT) to arrive at the final solution. 


## running
install [SageMath](https://doc.sagemath.org/html/en/installation/index.html) first.
```
sage -python ingonyama-2023/safe_bn254/solution.py
```
