#!/bin/bash
python3 fakewords.py > temp.txt
cat flag.txt >> temp.txt
cat temp.txt | perl -MList::Util=shuffle -wne 'print shuffle <>;' > singular.txt
rm temp.txt

echo "File generated, line count: $(wc -l < singular.txt)"

echo "Testing for unique flags with unique length - only 33 must appear!"
cat singular.txt | sort | uniq -u | awk '{ print length }' | sort | uniq -u

echo 'Testing flag - must appear once, with length 33'
cat singular.txt | sort | uniq -u | awk '{ print length, $0 }' | sort -n -s | grep "33 "

zip -r singular.zip singular.txt
mv singular.zip ../files
rm singular.txt