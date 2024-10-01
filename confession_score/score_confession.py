import librosa
import numpy as np
from pydub import AudioSegment

def analyze_audio(file_path):
    # Load the audio file
    y, sr = librosa.load(file_path)

    # Calculate duration
    duration = librosa.get_duration(y=y, sr=sr)

    # Calculate loudness
    audio = AudioSegment.from_wav(file_path)
    loudness = audio.dBFS  # dB full scale, average loudness

    # Calculate pitch variation (standard deviation of the pitch)
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    pitch_values = pitches[np.nonzero(pitches)]  # Get non-zero pitch values
    pitch_variation = np.std(pitch_values) if len(pitch_values) > 0 else 0

    # Calculate silence (count of zero-energy frames)
    energy = np.sum(librosa.feature.rms(y=y), axis=0)
    silence_frames = np.sum(energy < np.mean(energy) * 0.1)

    # Generate a "score" based on these factors
    score = (duration * 0.2) + (loudness * 0.3) + (pitch_variation * 0.3) + (silence_frames * 0.2)
    return score, duration, loudness, pitch_variation, silence_frames

# Example usage
audio_file = "confession_1727745250.47.wav"
score, duration, loudness, pitch_variation, silence_frames = analyze_audio(audio_file)
print(f"Score: {score}, Duration: {duration}, Loudness: {loudness}, Pitch Variance: {pitch_variation}, Silences: {silence_frames}")

