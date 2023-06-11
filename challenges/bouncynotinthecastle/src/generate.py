from PIL import Image
import random

f = open('src/qrcode.png', 'rb')
img = Image.open(f)

X0 = 20
Y0 = 20
STEP = 13
SIZE = 21

w, h = img.size

pix = img.load()
print(img.size)
print(pix[20,20])

def getRandomColor(color):
    r = 127 + random.randint(0, 128)
    g = 127 + random.randint(0, 128)
    b = 127 + random.randint(0, 128) 
    if color:
        b = b | 1
    else:
        b = b & 0xfe
    return '%02x%02x%02x' % (r, g, b)

print("READ QR Code")
print("")
out = ""
for y in range(0, SIZE ):
    s = ""
    for x in range(0, SIZE):
        val = pix[X0 + x * STEP, Y0 + y * STEP]
        out += getRandomColor(val)
        if val == 1:
            s += "00"
        else:
            s += "  "
    print(s)
print("")
print(out)

f = open("docker/app/background.png.js", "w")
f.write('hex="{}"'.format(out))
f.close