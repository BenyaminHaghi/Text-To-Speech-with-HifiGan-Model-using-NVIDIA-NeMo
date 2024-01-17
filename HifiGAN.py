#author: Benyamin Haghi
# Import necessary modules for FastPitch Model
from nemo.collections.tts.models import FastPitchModel

# Load the FastPitch model pretrained on NVIDIA dataset
# FastPitch is a text-to-speech model known for its speed and quality
spec_generator = FastPitchModel.from_pretrained("nvidia/tts_en_fastpitch")

# Import necessary modules for HifiGan Model
from nemo.collections.tts.models import HifiGanModel

# Load the HifiGan model pretrained on NVIDIA dataset
# HifiGan is used as a vocoder to generate high-fidelity audio
vocoder = HifiGanModel.from_pretrained("nvidia/tts_hifigan")

# Generate audio from text
import soundfile as sf

# Parse the text input for the speech synthesis
parsed = spec_generator.parse("Hi PyData. this is FastPitch with Hifi-Gan TTS from NeMo.")

# Generate spectrogram from parsed text using FastPitch
spectrogram = spec_generator.generate_spectrogram(tokens=parsed)

# Convert the generated spectrogram to audio using the HifiGan vocoder
audio = vocoder.convert_spectrogram_to_audio(spec=spectrogram)

# Save the synthesized audio to a file
# The audio is saved in WAV format at a sample rate of 22050 Hz
sf.write("speech.wav", audio.to("cpu").detach().numpy(), 22050)
