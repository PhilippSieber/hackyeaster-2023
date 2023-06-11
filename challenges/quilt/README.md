# solution
- Linux with Image Alchemy and zbarimg
- `convert -crop 69x69 quilt.png tiles.png`
- ``` a=""; for i in `seq 0 699` ; do a="$a`zbarimg -q tiles-${i}.png | awk -F':' '{ print $2 ; } ;'`" ; done; echo $a ```

## Text that should be recovered from the quilt:
Hello! Do you love quilts? Well... I am pretty sure I do! They are so pretty.. my oh my, but look at me getting lost in idle thoughts! You are here for an egg, right? I bet you are. Where did I put it? Ah, here he2023{this_is_th... No, sorry, that is not it. That was an old one, can you believe it? This maybe? he2023{I_need_this_egg_for_breakfast}. Nooo.. sorry! But I am fairly sure this is it, right here he2023{Qu1lt1ng_is_quit3_relaxing!} Yeah, that should be it. Sorry. I am rambling, but it is so nice to have a visitor appreciating my quilts! They are a lot of work, and I love all of them. Please, do not leave so soon. How about a cookie? Would you like a cookie? Hey, where are you going?

# generate
- Write a new solution.txt in src
- run `generate.sh`
- Info - actual tiling depends on the length of the new message; "`-tile 25x`" in the montage sets the amount of QR-codes in the X-Axis of the quilt.
- The colouring of some tiles is random and has no significance for the solution.

# additional info
## Cover image CC0 
Image by <a href="https://pixabay.com/users/placidplace-25572496/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7710530">Peace,love,happiness</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7710530">Pixabay</a>

