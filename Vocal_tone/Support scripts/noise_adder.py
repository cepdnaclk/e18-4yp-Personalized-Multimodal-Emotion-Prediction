import numpy as np
import soundfile as sf
import librosa
import numpy as np
import soundfile as sf
import os

def add_periodic_noise(audio, sr, noise_level):
    t = np.linspace(0, len(audio) / sr, num=len(audio))
    noise_modulation = noise_level * (np.sin(2 * np.pi * t / 1.7) + 1) / 2
    noise = np.random.normal(scale=noise_modulation)
    noiseUni = np.random.normal(scale=0.005, size=len(audio))
    return audio + noise + noiseUni

def add_uniform_noise(audio, noise_level):
    noise = np.random.uniform(-1, 1, size=len(audio))
    return audio + (noise_level * noise)

def add_gaussian_noise(audio, noise_level):
    noise = np.random.normal(scale=noise_level, size=len(audio))
    return audio + noise

def add_pink_noise(audio, noise_level):
    # Generate pink noise using a filter
    pink_noise = np.random.randn(len(audio))
    pink_noise = np.convolve(pink_noise, np.array([1, 0.5, 0.25]), mode='same') / 1.75
    return audio + (noise_level * pink_noise)

def add_noise_to_audio(type, audio_path, output_path, noise_level):
    # Load the audio file
    audio, sr = librosa.load(audio_path, sr=None)
    file_name = os.path.basename(audio_path)
    
    # Add noise to the audio
    if "uni" in type:
        noisy_audio = add_uniform_noise(audio,0.04)
        # Normalize audio to ensure it stays within bounds [-1, 1]
        max_val = np.max(np.abs(noisy_audio))
        if max_val > 1:
            noisy_audio /= max_val
        sf.write(output_path + 'Uniform\\'+ Class + '\\' + file_name, noisy_audio, sr)
    
    if "gau" in type:
        noisy_audio = add_gaussian_noise(audio,noise_level)
        max_val = np.max(np.abs(noisy_audio))
        if max_val > 1:
            noisy_audio /= max_val
        sf.write(output_path + 'Gaussian\\'+ Class + '\\' + file_name, noisy_audio, sr)

    if "per" in type:
        noisy_audio = add_periodic_noise(audio,sr,noise_level)
        max_val = np.max(np.abs(noisy_audio))
        if max_val > 1:
            noisy_audio /= max_val
        sf.write(output_path + 'Periodic\\'+ Class + '\\' + file_name, noisy_audio, sr)

    if "pin" in type:
        noisy_audio = add_pink_noise(audio,0.007)
        max_val = np.max(np.abs(noisy_audio))
        if max_val > 1:
            noisy_audio /= max_val
        sf.write(output_path + 'Pink\\'+ Class + '\\' + file_name, noisy_audio, sr)
    

# Example usage
Class = 'Neutral'
folder_path = 'C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Vocal\SplittedClear\\' + Class
output_audio_path = 'C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Vocal\SplittedNoisy\\'

files = os.listdir(folder_path)
# Iterate through each file and rename it
for index, file_name in enumerate(files):
    input_audio_path = os.path.join(folder_path, file_name)
    add_noise_to_audio(["uni","gau","per","pin"],input_audio_path, output_audio_path, 0.01)