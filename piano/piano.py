from minimix import minimix
raw_input('')
from minimix.quick import *

wav_file = toWav('./sounds/pianoc.ogg')

sf_folder = shifts(wav_file, range(-36, 13))

cf_file = cf(sf_folder, 'keyboards/pianoc.kb')

minimix(cf_file)
