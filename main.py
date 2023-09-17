import soundfile as sf
import pyloudnorm as pyln
import os

path = "/Users/nicolas.schmidt/MIX_FINAL"
target = -20.0

# iterate over all files in the directory
for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == ".wav":
        data, rate = sf.read(os.path.join(path, filename)) # load audio (with shape (samples, channels))
        meter = pyln.Meter(rate) # create BS.1770 meter
        loudness = meter.integrated_loudness(data) # measure loudness
        print(filename, loudness) # returns loudness (in LUFS)
        # normalize loudness
        print("Normalizing {0} to {0} LUFS".format(filename, target))
        normalized_audio = pyln.normalize.loudness(data, loudness, target)
        file_name = os.path.splitext(filename)[0] + "NORM.wav"
        full_path = os.path.join(path, file_name)
        sf.write(full_path, normalized_audio, rate, subtype='PCM_24') # save normalized audio
