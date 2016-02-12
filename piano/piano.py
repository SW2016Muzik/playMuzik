from minimix import minimix
raw_input('')
from minimix.quick import *

wav_file = toWav('./sounds/pianoc.ogg')

sf_folder = shifts(wav_file, range(-16, 16))

cf_file = cf(sf_folder, 'keyboards/pianoc.kb')

minimix(cf_file)
