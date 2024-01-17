# Text-to-Speech Synthesis using NeMo
This repo hosts a Python script for text-to-speech conversion using NVIDIA's NeMo, featuring FastPitch for synthesis and HifiGan for audio clarity. It's user-friendly, customizable, and ideal for AI speech tech enthusiasts. Contributions are welcome!

Overview

Welcome to the Text-to-Speech Synthesis repository! This Python script utilizes NVIDIA's NeMo toolkit to convert text into natural-sounding speech. It features the FastPitch model for rapid and high-quality speech synthesis and the HifiGan model for generating clear, high-fidelity audio.

Features
Fast and High-Quality Speech Synthesis: Uses NVIDIA's FastPitch for quick and high-quality speech synthesis.
High-Fidelity Audio: Employs HifiGan to transform synthesized speech into clear, high-fidelity audio.
Customizable: Change the input text to generate various speech outputs.
User-Friendly: Easy to run in any standard Python environment.
Requirements
Python
NVIDIA NeMo toolkit (pip install nemo_toolkit[tts])
Soundfile library (pip install soundfile)

How to Use
Clone the repository to your local machine.
Install the required dependencies.
Run the script in Python to convert the default text to speech.
Modify the input_text in the script for different outputs.

Code Overview
FastPitch Model Loading: Loads FastPitch for speech synthesis.
HifiGan Model Loading: Uses HifiGan as a vocoder to convert spectrograms to audio.
Text-to-Speech Conversion: Converts text to speech, involving text parsing, spectrogram generation, and audio conversion.
Saving the Output: Saves the final audio as a .wav file.

Contributions
Your contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.
