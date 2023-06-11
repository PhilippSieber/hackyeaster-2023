# solution
- run `python3 src/solve.py` and scan QR code
- manual solution
  - inspect the javascript source
  - dump the `hex` variable
  - find it's a 21x21 array of 6 digit hex values (colours)
  - look at last bit -> even: 0, odd: 1
  - scan QR code

# generate 
- Get QR Code from https://goqr.me/, export as PNG, 300px, must be sized 21x21
- Save QR Code in src/qrcode.png
- Run `python3 src/generate.py`