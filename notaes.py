import codecs

from Cryptodome.Cipher import AES
import os

key = os.urandom(16)
nonce = os.urandom(8)
flag = b"ictf{streeeeeeeeeem_ciphers_are_cooooooooooool}"
notflag = b"The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."

cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
print(f"enc = {cipher.encrypt(flag)}")

cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
print(f"dec = {cipher.decrypt(notflag)}")

enc = b'\x99gW\xcb\xb1(\xa8\xa6@\xca\xedT\x9c\xa6\xeb\x1cH,\x86A\xcbYj|\xb0\x1f PXI\x83\x86\nc7\xb8[\x86\x888\xc7\\D-\x17\xf1\xe7'
dec = b'\xa4lF\x8d\x8c2\xa8\xba@\xdc\xfbv\x8b\xa2\xe3Y}(\x88{\xda\x10Nq\xa6\x19sfJ\x1b\x87\xf9\x04y4\xa3]\x9a\x936\xcfV\x0b#\x1d\xef\xf5\x83\x91\x0b\x0e\x1d\xd1\xec|\xba\xb8\x08\xb5\xb09r5b\xa40\xb3\x9e\x93\xdd\\\x1b\xe5r\x85@\xf5\x9f\r:\xc6 0\x88\xa6\xfdje\xec\x1dK\x8d\x04\xcfj\t\x19\x0exQ(\xf0\xbaw\xc1\xeb_c\xea\x13\xc0\x884\x80\x82<\\A:q}\xb2}\xf4n\xfa\xf4\x9f\xb9\xe2\x11\xec\xdfP\xfa\xfd\xf3\x1dg)\x9d\x08<\x86@\x99\x90-!\x91\xc1\x87\xe2\xbf!\xdb\xb4X7X\xa4mz\xba\x16\xbb\xc4\x7fNO\xeb\xa5\t\xa6\x18Q|\xd0/\xcbCo2\xfa\xb2K\xd5\x99\x8a\xccG1\xba\xd3\x8c\xe0\xca\x17\xef/A \x95\xc5\xdbf8jx\xc3\xdf\xa5\xcbl\xea\x99\xd9\x89g\x91\x89)o\xcb\xb4\xacJ\x87\x15\x8f1\x0e\xf4~\xeb\xaf\x07\xe8)0\xb9\x83\xbc\x94\xb2\x8fW\x17\xa6\x13\x04\x15\x9c\xd7\x9b\xe7\tU\x9a\xa7Hb\x02\x9fY\xa1+\xc9\n\x16\x0b\xfc\xb0pZ\x00\xdc\xfa)\xa3\xa79\x9f(#A\x9a`\xbbA\xfe\x96DC\x81\x81\x89$\xaeM\x18I\xe2\\\x8a E\xfa\x1e\x88\xb9HnU\xedEzS\xe8\xd7H\xa5\xdd_\xd1L\xa2{q\x90\x19\xe5v\xcf\x83\x1d^\x7f\xa2tqg\xddu3\xbb\xf2\x1c\xfd\xb4s9\xd3C2r\xf1\xe4,\x9d\xd4\x85\x0e>\x86\xcc\xd5\x10\xfe\x98r\xff7`\x80y$`\x85F\xff\x9b\xfc\xacu\xd0YU\x13*\xac\x91\xc21\x9e\xac\xf1\xd7\xa6-\xca{J\xf8\x989\xf2\x975\x16\xe6\xe2\x0b8\x9c\t+\xf7\xb0a\x95lRXe\xb8f\xb3\xe1\x1b\x97E\xd0\xc7HV\xa2\x7f\xcc\x89\xfb\\E\x18\x10\x8bG\x00}o\xe1\x0cn\xc1\xa7y\x84\xde\x96\xf8\xe6U\t\x1ei\xac\xe6q\x13\xf40\xfb\x85%\xbe\x93\xa7\x12^\xbcz\xea\xc8\x14!\xf2\xb0\xa6`m\xed\xedo+\x85\xc8\xec\xf0\xb4\xbfA\x04x\xf6T\xf1\x9e\xdbN}\x1d\x8a\xc84\x1e\x19Y\x19\xf9\x81\xc9\x1c\x91\xc1\xc9\xfbC\x1764\x16\x98\x97\xe0`O\xcb,\x14A\xf34\xf9<\xc0P\x01\xd5+\xd4\xfcyYW\xad\x8c\x08R\xb9^\xd9\x1d\xb0\xe5P\x81H\xab"\xd72:\xc0\xf8K'


# https://crypto.stackexchange.com/questions/79854/repeating-nonce-in-ctr-mode
# https://crypto.stackexchange.com/questions/2932/how-can-i-find-two-strings-m-1-and-m-2-knowing-that-i-know-m-1-oplus-m-2

def XOR1(s1, s2):
    return ''.join(chr(a ^ b) for a, b in zip(s1, s2))


def XOR2(i1, i2):
    return ''.join(chr(ord(a) ^ b) for a, b in zip(i1, i2))


result_1 = XOR1(enc, notflag)
print(XOR2(result_1, dec))