#!/usr/share/asterisk/pyvm/bin/python3

import sys
import os
import subprocess
import librosa
import numpy as np
from pydub import AudioSegment

# Function to parse AGI environment variables from Asterisk
def get_agi_variable(name):
    for line in sys.stdin:
        if line.startswith(name):
            return line.split(":")[1].strip()
    return None

# Function to perform quantitative analysis on the confession WAV file
def analyze_audio(file_path):
    # Load the audio file with librosa (WAV format)
    y, sr = librosa.load(file_path, sr=None)

    # Analyze duration
    duration = librosa.get_duration(y=y, sr=sr)

    # Analyze loudness using pydub
    audio_segment = AudioSegment.from_wav(file_path)
    loudness = audio_segment.dBFS  # dB relative to full scale

    # Analyze pitch variation
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    pitch_values = [p for p in pitches if p > 0]
    pitch_variation = np.std(pitch_values) if pitch_values else 0

    # Analyze pauses (silences)
    silence_threshold = -30.0  # Adjust this threshold for detecting silence
    silences = librosa.effects.split(y, top_db=30)
    num_silences = len(silences)

    # Compute a simple "score" based on the metrics
    score = duration * (np.abs(loudness) + pitch_variation + num_silences)

    return score

# Main function to handle AGI interaction
def main():
    # Read UNIQUEID from Asterisk (passed from the dialplan)
    unique_id = get_agi_variable("agi_arg_1")

    # Define the path to the confession recording based on UNIQUEID
    file_path = f"/var/spool/asterisk/confessions/confession_{unique_id}.wav"

    # Ensure the file exists before proceeding
    if not os.path.exists(file_path):
        print(f"VERBOSE \"File {file_path} does not exist!\" 1")
        sys.exit(1)

    # Analyze the audio file and calculate a score
    score = analyze_audio(file_path)

    # Print the result (you can also pass it back to Asterisk or save it)
    print(f"VERBOSE \"Confession score for {unique_id}: {score}\" 1")

    # Output the result to Asterisk (optional: could return it in the dialplan)
    print(f"SET VARIABLE confession_score {score}")

if __name__ == "__main__":
    main()

