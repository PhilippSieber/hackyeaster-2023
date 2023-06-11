#!/bin/bash
mkdir tiles 2>/dev/null
cat solution.txt | ./quilter.sh
montage tiles/*.png -geometry +0+0 -tile 25x newquilt.png