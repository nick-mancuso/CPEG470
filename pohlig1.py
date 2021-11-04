from Cryptodome.Util.number import *
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import hashlib
import random
import os

flag = b"REDACTEDFLAGHERE"


def getSmallPrimes(n):
    nums = range(2, n)
    primes = []
    while len(nums) > 0:
        prime = nums[0]
        nums = list(filter(lambda x: x % prime, nums))
        primes.append(prime)
    return primes


primes = getSmallPrimes(100000)


def getWeakProd(nbits):
    temp = 1
    cutoff = 1 << nbits
    while temp < cutoff:
        temp *= random.choice(primes)
    return temp


def getWeakPrime(nbits):
    p = 2 * getWeakProd(nbits - 1) + 1
    while not isPrime(p):
        p = 2 * getWeakProd(nbits - 1) + 1
    return p


p = getWeakPrime(1024)
assert (isPrime(p))
g = 3
farts = []
temp = g
for i in range(2000000):
    farts.append(temp)
    temp = (temp * g) % p
assert (len(farts) == len(set(farts)))


def pickSecretKey(p):
    a = getRandomRange(3, p - 2)
    while GCD(a, p - 1) != 1:
        a = getRandomRange(3, p - 2)
    return a


a = pickSecretKey(p)
publicKey1 = pow(g, a, p)
b = pickSecretKey(p)
publicKey2 = pow(g, b, p)

secretNum = pow(publicKey1, b, p)
secretNum2 = pow(publicKey2, a, p)
assert (secretNum == secretNum2)

skh = hashlib.sha256(long_to_bytes(secretNum)).digest()
IV = os.urandom(16)

cipher = AES.new(skh, IV=IV, mode=AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(flag, 16))

testcipher = AES.new(skh, IV=IV, mode=AES.MODE_CBC)
assert (flag == unpad(testcipher.decrypt(ciphertext), 16))

print("p = %d" % p)
print("g = %d" % g)
print("publicKey1 = %d" % publicKey1)
print("publicKey2 = %d" % publicKey2)
print("IV_hex = %s" % IV.hex())
print("ciphertext_hex = %s" % ciphertext.hex())
