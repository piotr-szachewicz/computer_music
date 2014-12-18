# create a synthetic 'sine wave' wave file with set frequency and length
# tested with Python25 and Python30  by vegaseat  28dec2008

import math
import wave
import struct
from random import *

def make_soundfile(freq=440, data_size=1000, filename="sine_wave1.wav"):
    """
    create a synthetic 'sine wave' wave file with frequency freq
    file has a length of about data_size*2 and the given filename
    """
    frate = 44100.0#11025.0  # framerate as a float
    amp = 4000.0     # multiplier for amplitude 

    length = 60;
    data_size = length * int(frate);

    modulation_frequency = 2.0

    play_tone = False;
    tone_frequency = 400.0;
    tone_length = frate/4;
    tone_position = 0;
    

    # make a sine list ...
    sin_list = []
    for i in range(data_size):
        val = 0.0;
#	if (random() > 0.995):
#		val = amp;

	if (random() > 0.9999 and not play_tone):
		play_tone = True;	
		tone_position = 0;
		tone_frequency = 60 + random() * 40;
		tone_length = frate/2 + random() * frate/2;

	if (play_tone):
		val += amp * math.sin(2*math.pi*tone_frequency*(i/frate))
		tone_position += 1;
		if (tone_position >= tone_length):
			play_tone = False;

	sin_list.append(val);
    wav_file = wave.open(filename, "w")

    # required parameters ...
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes = size
    comptype = "NONE"
    compname = "not compressed"

    # set all the parameters at once
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, 
        comptype, compname))

    # now write out the file
    print("may take a few seconds ...")
    for s in sin_list:
        # write the audio frames, make sure nframes is correct
        wav_file.writeframes(struct.pack('h', s))
    wav_file.close()
    print( "%s written" % filename)


# set some variables ...
freq = 440.0
size = 40000  # data size, file size will be about twice that

# write the synthetic wave file to ...
filename = "WaveTest2.wav"

make_soundfile(freq, size, filename)
