#!/bin/bash
while read ALINE
do
    for ((i=0; i < ${#ALINE}; i++))
    do
        j=$(printf "%03d" ${i})
        ACHAR=${ALINE:i:1}
        echo $j $ACHAR
        qrencode "$ACHAR" -m 1 -o tiles/${j}.png

        if [ $(($RANDOM % 7)) -eq 0 ]; then 
            mogrify -channel red -negate tiles/${j}.png
        #fi
        #elif [ $(($RANDOM % 11)) -eq 0 ]; then 
            #mogrify -channel green -negate tiles/${j}.png # zbarimg can't read this
        #fi
        elif [ $(($RANDOM % 19)) -eq 0 ]; then 
            mogrify -channel blue -negate tiles/${j}.png
        fi

    done
done

