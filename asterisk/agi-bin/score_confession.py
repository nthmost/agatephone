#!/usr/bin/env python3

import sys
import librosa
import numpy as np
from pydub import AudioSegment
import os

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
    silences = librosa.effects.split(y, top_db=30)
    num_silences = len(silences)

    # Compute a simple "score" based on the metrics
    score = duration * (np.abs(loudness) + pitch_variation + num_silences)
    
    return score

def main():
    if len(sys.argv) != 2:
        print("Usage: score_confession.py <UNIQUEID>")
        sys.exit(1)

    unique_id = sys.argv[1]
    
    # Path to the recorded confession file
    file_path = f"/var/spool/asterisk/confessions/confession_{unique_id}.wav"

    if not os.path.exists(file_path):
        print(f"File {file_path} not found!")
        sys.exit(1)

    # Perform audio analysis and calculate the score
    score = analyze_audio(file_path)

    # Log the score for debugging or further processing
    print(f"Confession score for {unique_id}: {score}")

    # Here, you could write the score to a log file, send it to another system,
    # or process it in any way you need.

if __name__ == "__main__":
    main()

