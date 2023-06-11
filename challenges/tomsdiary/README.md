# solution
- note that the title lines are not regular
  - `\/\ \\\/ / \/\ /\\ /\ \/\ //\ /\/ /\// //\/ /\// /\/ //\ /\\\ \\/\`
- find out that it is the Tom Tom Code
- decode it, e.g. using https://gc.de/gc/atomtom/
  - slashesforprofit
- base64-decode the string in the diary, and find out it's a zip file
  - e.g. using the `file`command
- unzip the file with the password from above

# generation
`echo "he2023{sl4sh3s_m4k3_m3_h4ppy}" > flag.txt && zip -r -P slashesforprofit flag.zip flag.txt | base64 -b 64 flag.zip`