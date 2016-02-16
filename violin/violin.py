from minimix import minimix
raw_input('')
from minimix.quick import *

wav_file = toWav('./sounds/violin.ogg')

sf_folder = shifts(wav_file, range(-16, 16))

cf_file = cf(sf_folder, 'keyboards/violin.kb')

minimix(cf_file)
