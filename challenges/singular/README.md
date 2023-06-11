# solution
- flag is unique
  - only appears once
  - length is unique
- `cat singular.txt | sort | uniq -u | awk '{ print length(), $0 | "sort -n" }' | grep 33`