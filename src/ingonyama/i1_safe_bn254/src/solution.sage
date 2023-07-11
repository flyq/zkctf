# BN-254 prime
p = 21888242871839275222246405745257275088696311157297823662689037894645226208583

# Generator
Gx = 14810849444223915365675197147935386463496555902363368947484943637353816116538
Gy = 742647408428947575362456675910688304313089065515277648070767281175728054553

# P = kG
Px = 5547094896230060345977898543873469282119259956812769264843946971664050560756
Py = 14961832535963026880436662513768132861653428490706468784706450723166120307238

F = GF(p)
E = EllipticCurve(F, [0, 2023])

print(E)
