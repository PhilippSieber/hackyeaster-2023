# solution

- CVE-2022-44268

- use `src/cve-2022-44268/craft.py` to generate a manipulated image
  - `python3 craft.py wizard-orig.png wizard-exploit.png /flag.txt`

- upload the image, download the flipped image

- use `src/cve-2022-44268/extract.py` to read the flag from the image
  - `python3 extract.py wizard-flipped.png`
  
- alternative: open with hex editor and decode ASCII
