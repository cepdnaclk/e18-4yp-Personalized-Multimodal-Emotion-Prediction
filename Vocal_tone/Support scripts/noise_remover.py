import librosa
import numpy as np

def remove_noise(audio_path, noise_level=0.02):
    # Load audio file
    y, sr = librosa.load(audio_path, sr=None)

    # Compute Short-Time Fourier Transform (STFT)
    D = librosa.stft(y)

    # Convert magnitude spectrogram to float array
    mag = np.abs(D).astype(float)

    # Estimate noise floor
    noise_floor = np.percentile(mag, 75, axis=1)

    # Mask elements where the magnitude is below the noise floor
    mask = mag > noise_level * noise_floor[:, np.newaxis]

    # Apply the mask to the complex STFT
    D_cleaned = D * mask

    # Inverse STFT to obtain cleaned signal
    y_cleaned = librosa.istft(D_cleaned)

    return y_cleaned, sr


# Example usage:
audio_path = 'C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\\audio.m4a'  # Provide the path to your audio file
cleaned_audio, sr = remove_noise(audio_path)

# Save the cleaned audio to a file
librosa.output.write_wav('C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\cleaned_audio.m4a', cleaned_audio, sr)
