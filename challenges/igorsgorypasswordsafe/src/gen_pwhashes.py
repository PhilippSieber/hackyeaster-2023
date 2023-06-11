import bcrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

print("LOGINS:")
salt = bcrypt.gensalt()
password = bcrypt.hashpw("gXJSEdx4dJwE8x3eXohx".encode('utf-8'), salt)
print("roy: {}".format(password))
salt = bcrypt.gensalt()
password = bcrypt.hashpw("ubYwnqgML9CgPdt8nkcs".encode('utf-8'), salt)
print("igor: {}".format(password))

print()
print("PW FOR VAULT:")
# generated with os.urandom(16) / os.random(32)
KEY = b'\x06\x0b\xda\xa02\xaa\xf8\n\xd4!\x1ag\xabI\x9f\xa7\xa6\x1f\xf9\xa1\x9e\xce\xbb\\n\xbf\xdd\xe7\t\xb9\x19\x06'

def encrypt(pw):
    AESService = AES.new(KEY, AES.MODE_CBC)
    enc = AESService.encrypt(pad(pw.encode("UTF-8"), AES.block_size))
    return b64encode(AESService.iv + enc).decode('utf-8')

def decrypt(pw):
    enc = b64decode(pw)
    iv = enc[:AES.block_size]
    AESService = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(AESService.decrypt(enc[AES.block_size:]), AES.block_size)

pws = {'he2023{1d0R_c4n_d3str0y_ur_Crypt0_3ff0rt}', 'verySecure', 'SQLI_doesnt_help', 'Well_not_the_flag', 'White_Rabbit_99'}

for p in pws:
    enc = encrypt(p)
    dec = decrypt(enc)
    print("{} --> {} --> {}".format(p, enc, dec)) 