# This AWS lambda is setup at:
# https://o5lyi532hb.execute-api.us-east-1.amazonaws.com/default/ecboracle?prefixhex=00112233

import json
import os
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

# prefix=00112233
# ciphertext=7077292b7c9790529096ac4f313a184cd8f6f6fad8b380f0984750e142f8947a8188b7f1de905161dfc27872e672e66a
# prefix=44556677
# ciphertext=3ca35cbe45f050ff2917712901ff9072d8f6f6fad8b380f0984750e142f8947a8188b7f1de905161dfc27872e672e66a
# A + C =    4cd475953967c0ad b981dd6630c5883e0000000000000000000000000000000000000000000000000000000000000000
# 00000000 = f590952db9acc795270e08c96ee87492 d8f6f6fad8b380f0984750e142f8947a8188b7f1de905161dfc27872e672e66a
# 00000001 = 5a328d4e88ae8d0d3c011132a478d1ee d8 f6 f6 fa d8 b3 80 f0 98 47 50 e1 42 f8 94 7a 81 88 b7 f1 de 90 51 61 df c2 78 72 e6 72 e6 6a
# 11111111 = d245185036f71db9 ca 46 e8 ef 1d 9b e485 d8f6f6fad8b380f0984750e142f8947a8188b7f1de905161dfc27872e672e66a
# aaaaaaaa = 92 e1 94 fe 1e 12 c8 7e 3b a8 ba 95 1f cc cb 33 d8f6f6fad8b380f0984750e142f8947a8188b7f1de905161dfc27872e672e66a
# 01 = 702a7d225474cbeec4ddc9d7c81d15a4 bda382a53d481f3bcdd47ffa49101b5a
# 11 = 53dd747f78ea260b 80fcc29f62862219 bda382a53d481f3bcdd47ffa49101b5a

# AAAAAAAAAAAAAAA = 8a07ad6428a927fa8f52e337d598951c34a15576af6ce5e8d03ebd85d45f89ab3552e14527fa2c3f9a216b7347dddbef
# AAAAAAAAAAAAAAA1 =


prefix = bytes.fromhex("00000000")
flag = "something"
padded = pad(prefix + flag.encode(), 16)
secretkey = "0000000000000000"
cipher = AES.new(secretkey.encode(), AES.MODE_ECB)
encrypted = cipher.encrypt(padded)

while not encrypted.hex().startswith("f590952db9acc795"):
    encrypted = cipher.encrypt(padded)
    secretkey = str(int(secretkey) + 1).zfill(16)
    print("secretKey = " + secretkey)
    cipher = AES.new(secretkey.encode(), AES.MODE_ECB)
    encrypted = cipher.encrypt(padded)
    # print(encrypted.hex())
    print(encrypted.hex())


