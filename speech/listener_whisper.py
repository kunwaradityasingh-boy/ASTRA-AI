from faster_whisper import WhisperModel
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import os

print("Loading Whisper Model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper Ready!")

print("Speak for 5 seconds...")

duration = 5
sample_rate = 16000

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

wav.write(temp.name, sample_rate, audio)

segments, info = model.transcribe(
    temp.name,
    language="hi",
    beam_size=5
)

print("\nYou said:")

for segment in segments:
    print(segment.text)
    
try:
    os.remove(temp.name)
except PermissionError:
    pass