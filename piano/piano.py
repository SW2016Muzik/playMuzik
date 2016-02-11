from minimix import minimix
raw_input('')
from minimix.quick import *

# transforms the .ogg file into a .wav file in '/sounds'
wav_file = toWav('./sounds/piano.ogg')

# creates a folder in '/soundfonts' with all the shifts of the pitches
sf_folder = shifts(wav_file, range(-25,25))

# creates a configuration file piano.cf in '/configs'
cf_file = cf(sf_folder, 'keyboards/piano.kb')

# launches minimix
minimix(cf_file)
