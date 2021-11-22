# run like this: sage -python pohlig_solver.py
# stolen from https://github.com/Chongsawad/Pohlig-Hellman/blob/master/pohlig.sage
from sage.all import *

p = 174594482216063332687991653533613063770426549745145666527514529480958822426370353643375830948813658634964823617721730693176608943341995371690658516774361830439602240387720356809695559821251907643159593886138136950548993670431910927254578346730227771171752157873528673600318122914183274510376878346690866613643
g = 2
pk1 = 0x1337133713371337133713371337133713371337

F = IntegerModRing(p)
g = F(g)
pk1 = F(pk1)
G = []
H = []
X = []
c = []
N = factor(p - 1)
for i in range(0, len(N)):
    G.append(g ** ((p - 1) / (N[i][0] ** N[i][1])))
    H.append(pk1 ** ((p - 1) / (N[i][0] ** N[i][1])))
    X.append(log(H[i], G[i]))
    c.append((X[i], (N[i][0] ** N[i][1])))

print("G=", G, "\n", "H=", H, "\n", "X=", X)

# Using Chinese Remainder
c.reverse()

for i in range(len(c)):
    if len(c) < 2:
        break
    t1 = c.pop()
    t2 = c.pop()
    r = crt(t1[0], t2[0], t1[1], t2[1])
    m = t1[1] * t2[1]
    c.append((r, m))

print("(x,p-1) =", c[0])
