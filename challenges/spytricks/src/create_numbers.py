#!/usr/bin/python3

# The egg is the result of a prime, 313, times the ASCII code of each letter
# The difficulty lies in finding the common denominator 313, from then on it's easy
# The spy coin is a diversion, but makes for interesting history.
# AFAIK the actual code breaking process has not been revealed.
# https://www.futilitycloset.com/2017/09/30/hollow-nickel-case/

egg="he2023{I_like_303_b3tter_but_thats_n0t_pr1me}"

padding_before = ""
padding_after = ""


padding_before += "WE CONGRATULATE YOU ON A SAFE ARRIVAL. WE CONFIRM THE RECEIPT OF YOUR LETTER TO THE ADDRESS V REPEAT V AND THE READING OF LETTER NUMBER 1.\n"
#padding_before += "FOR ORGANIZATION OF COVER, WE GAVE INSTRUCTIONS TO TRANSMIT TO YOU THREE THOUSAND IN LOCAL (CURRENCY). CONSULT WITH US PRIOR TO INVESTING IT IN ANY KIND OF BUSINESS, ADVISING THE CHARACTER OF THIS BUSINESS.\n"
#padding_before += "ACCORDING TO YOUR REQUEST, WE WILL TRANSMIT THE FORMULA FOR THE PREPARATION OF SOFT FILM AND NEWS SEPARATELY, TOGETHER WITH (YOUR) MOTHER’S LETTER.\n"

#padding_after = "IT IS TOO EARLY TO SEND YOU THE GAMMAS. ENCIPHER SHORT LETTERS, BUT THE LONGER ONES MAKE WITH INSERTIONS. ALL THE DATA ABOUT YOURSELF, PLACE OF WORK, ADDRESS, ETC., MUST NOT BE TRANSMITTED IN ONE CIPHER MESSAGE. TRANSMIT INSERTIONS SEPARATELY.\n"
padding_after += "THE PACKAGE WAS DELIVERED TO YOUR WIFE PERSONALLY. EVERYTHING IS ALL RIGHT WITH THE FAMILY. WE WISH YOU SUCCESS. GREETINGS FROM THE COMRADES. NUMBER 1, 3RD OF DECEMBER.\n"

my_prime = 313

padded_egg = padding_before + egg + "\n" + padding_after

ascegg=""
ctr = 0

for i in padded_egg:
	ascegg += f"{my_prime * ord(i):05} "
	ctr += 1
	if ctr >= 10:
		ascegg += "\n"
		ctr = 0
	
print(f"Egg clear: {egg}\nEgg crypt: \n{ascegg}\n")

# now to proof it's working

my_parts = ascegg.split()
my_unscrambled_egg = ""
for i in my_parts:
	my_unscrambled_egg += chr(int(int(i) / my_prime))

print(my_unscrambled_egg)