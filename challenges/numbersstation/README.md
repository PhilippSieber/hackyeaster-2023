# solution
- convert numbers.mp3 to .wav
- manually transcribe all "0"s (cero) and "1"s (uno) -> boring but doable OR
- get Google to to the job for you by Speech-To-Text recognition
- important - ignore every second number (2-9) and only use 0s and 1s!
- The resulting binary string, converted to ASCII, gives the flag.

See `src/solve.py`.

# notes
- the numbers between the zeroes and ones are randomly generated and have no significance
- needed to put *something* in between the 0s and 1s, because the free Speech-To-Text API from Google wouldn't understand three 0s in a row and shorten it to two 
- The code for recognition comes from here: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python .