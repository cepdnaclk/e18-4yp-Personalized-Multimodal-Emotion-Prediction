import numpy as np
import librosa
import soundfile as sf

def spectral_subtraction(audio_file, noise_clip):
    # Load the noisy audio and noise clip
    noisy_audio, sr = librosa.load(audio_file, sr=None)
    noise, _ = librosa.load(noise_clip, sr=None)

    # Perform Short-Time Fourier Transform (STFT) on the audio and noise
    noisy_stft = librosa.stft(noisy_audio)
    noise_stft = librosa.stft(noise)

    # Compute the magnitude spectrogram of the noisy audio and noise
    mag_noisy = np.abs(noisy_stft)
    mag_noise = np.abs(noise_stft)

    # Estimate the noise spectrum by taking the minimum magnitude across time
    noise_spectrum = np.min(mag_noise, axis=1, keepdims=True)

    # Apply spectral subtraction
    mag_clean = np.maximum(mag_noisy - noise_spectrum, 0)

    # Reconstruct the cleaned audio signal from the modified magnitude spectrogram
    phase = np.angle(noisy_stft)
    # Use np.float64 instead of np.float
    clean_stft = mag_clean * np.exp(1j * phase)
    clean_audio = librosa.istft(clean_stft, dtype=np.float64)

    return clean_audio, sr

# Example usage
if __name__ == "__main__":
    # Specify paths to the noisy audio file and the noise clip
    noisy_audio_file = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Vocal\Original\\noisy_clip.m4a"
    noise_clip = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Vocal\Original\\noise.m4a"

    # Perform spectral subtraction
    clean_audio, sr = spectral_subtraction(noisy_audio_file, noise_clip)

    # Save the cleaned audio to a new file
    output_file = "cleaned_audio.m4a"
    sf.write(output_file, clean_audio, sr)
    print("Cleaned audio saved to", output_file)
