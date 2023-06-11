#!/usr/bin/python3

# requirements: pip3 install gtts playsound SpeechRecognition pydub
# code mostly from https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
# bugs all mine

import gtts

import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

import random

def convert_mp3_to_wav(mp3file, wavfile):
	sound = AudioSegment.from_mp3(mp3file)
	sound.export(wavfile, format="wav")

def speech_to_text(my_wavfile):
	r = sr.Recognizer()

	# open the file
	with sr.AudioFile(my_wavfile) as source:
	    # listen for the data (load audio to memory)
	    audio_data = r.record(source)
	    # recognize (convert from speech to text)
	    text = r.recognize_google(audio_data, language="es-ES")
	    return(text)

# That's the flag
egg_cleartext = "he2023{L1stening_to_spy_c0mmunicat1ons}" 

# convert the mp3 to wav
print("converting to wav...")
convert_mp3_to_wav("./numbers.mp3", "./numbers.wav")
print("...done")

# And now let google do the heavy lifting
egg = speech_to_text("./numbers.wav")
print("speech to text done")

split_egg = egg.split()

my_ctr = 0 

bin_egg = ""

for my_number in split_egg:
	print(my_number)
	if my_number.lower() == "cero" or my_number.lower() == "cero.":
		bin_egg += "0"
	#	my_ctr = my_ctr + 1
	elif my_number.lower() == "uno" or my_number.lower() == "uno.":
		bin_egg += "1"
	#	my_ctr = my_ctr + 1
	else:
		# print(f"error {my_number}") # debug
		pass

n = int(bin_egg, 2)
egg_flag =n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

print(f"\nEgg before: {egg_cleartext}\nEgg after : {egg_flag}")
if egg_cleartext == egg_flag:
	print("Match")















