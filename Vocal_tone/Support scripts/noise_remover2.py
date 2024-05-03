import numpy as np
import librosa
from scipy.io import wavfile

def remove_noise(audio_path, noise_duration=2.0):
    # Load the audio file
    audio, sr = librosa.load(audio_path, sr=None)

    # Estimate noise from a silent segment
    silent_duration = noise_duration * sr
    noise_profile = np.mean(np.abs(audio[:int(silent_duration)]))

    # Perform noise reduction
    reduced_audio = audio - noise_profile

    return reduced_audio, sr

# Example usage
audio_path = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Vocal\Original\\neutral.opus"

cleaned_audio, sr = remove_noise(audio_path)

# Save the cleaned audio
wavfile.write("C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Vocal\Original\\cleaned_happy.wav", sr, cleaned_audio.astype(np.float32))