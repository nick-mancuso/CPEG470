# run like this: sage -python pohlig_solver.py
# stolen from https://github.com/Chongsawad/Pohlig-Hellman/blob/master/pohlig.sage
from sage.all import *

p = 792321885721039223055203621511476008103176341524490283402628477451813722842720337402795900165653052271349918359044973129279701490613980973589891701136745034631765803279015068621842643130239591656504870040900517665771748667093361827700044850800239770001931593567314982414093813968959529405924117755593099360943
g = 3
h = 710875014521586133177240861275411954502274981112927572082940815173504661025454567548435293794165742619652743188632359986402946530631590657230251177397188927619054747566071728206203495270418156469763404027680754983935556040450591504717450568526386336795569263884391363832901921960805323527167470059092379137922

F = IntegerModRing(p)
g = F(g)
h = F(h)
G = []
H = []
X = []
c = []
N = factor(p - 1)
for i in range(0, len(N)):
    G.append(g ** ((p - 1) / (N[i][0] ** N[i][1])))
    H.append(h ** ((p - 1) / (N[i][0] ** N[i][1])))
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
