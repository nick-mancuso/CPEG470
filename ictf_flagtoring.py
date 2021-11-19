from math import gcd
from random import randrange
from Cryptodome.Util.number import long_to_bytes

import sympy

# given from ictf:
# from secret import get_e
# from gmpy2 import next_prime
# import random
#
# with open("flag.txt", "rb") as f:
#     flag = int.from_bytes(f.read().strip(), "big")
#
# p = next_prime(flag << 2)
# p = flag * 2**2 # same as above
# q = next_prime(random.randrange(2**p.bit_length()))
#
# n = p * q
# e = get_e(p, q, n)
#
# print(f"{n = }")
# print(f"{e = }")
# print(f"{pow(int.from_bytes(b'Have a message: flagtoring', 'big'), e, n) = }")

# given output from ictf:
# n = mpz(1528656555903550344116452290097825083432239562289311449762856110644178238847468718159931142582566958406852960634326674294592831730135914025243113420620191820735271996685130044674881553230289164686150060478587182721212339660071286119)
# e = 764328277951775172058226145048912541716119781144655724881428055322089119423734359079965571291283479203426480317163292925665158834567666283670763086349732720212733069060883710729256895758575480803498007307124796853534451106915539873
# pow(int.from_bytes(b'Have a message: flagtoring', 'big'), e, n) = mpz(116311321092553636586360715178833872761109494107849766482832999)

_n = 1528656555903550344116452290097825083432239562289311449762856110644178238847468718159931142582566958406852960634326674294592831730135914025243113420620191820735271996685130044674881553230289164686150060478587182721212339660071286119
_e = 764328277951775172058226145048912541716119781144655724881428055322089119423734359079965571291283479203426480317163292925665158834567666283670763086349732720212733069060883710729256895758575480803498007307124796853534451106915539873
_d = 1


# Returns a tuple (r, t) | n = r*2^t
# Complexity O(lg n)*
def remove_even(n):
    if n == 0:
        return 0, 0
    r = n
    t = 0
    while (r & 1) == 0:
        t = t + 1
        r = r >> 1
    return r, t


# Returns a non-trivial sqrt(1) mod N, or None
# Arguments:
#     x: random integer 2 <= x < N
#     k: multiple of lambda(N)
#     N: modulus
# Complexity O((lg n)^3)
def get_root_one(x, k, n):
    (r, t) = remove_even(k)
    z = None
    i = pow(x, r, n)
    while i != 1:
        z = i
        i = (i * i) % n
    if z == n - 1:
        return None  # trivial
    return z


# Returns a tuple (p, q) that are
# the prime factors of N, given an
# RSA key (e, d, N)
def factor_rsa(e, d, n):
    k = e * d - 1
    y = None
    while not y:
        x = randrange(2, n)
        y = get_root_one(x, k, n)
    p = gcd(y - 1, n)
    q = n // p
    return p, q

# theory: https://crypto.stackexchange.com/questions/62482/algorithm-to-factorize-n-given-n-e-d
# lot of code from: https://crypto.stackexchange.com/questions/6361/is-sharing-the-modulus-for-multiple-rsa-key-pairs-secure/14713


_p, _q = factor_rsa(_e, _d, _n)
assert (_p * _q == _n)
prev_prime = sympy.ntheory.generate.prevprime(_p)
flag = prev_prime // 4
print(flag)
print(long_to_bytes(flag))
