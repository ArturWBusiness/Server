import pyaudio
import numpy as np

RATE    = 16000
CHUNK   = 256

p = pyaudio.PyAudio()

player = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True,
frames_per_buffer=CHUNK)
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
maxx = 1000
def listen(s):
    for i in range(int(2*s*RATE / CHUNK)):  # do this for 10 seconds
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        print(data)
        player.write(data, CHUNK)

while True:
    input("Read")
    listen(20)
stream.stop_stream()
stream.close()
p.terminate()
