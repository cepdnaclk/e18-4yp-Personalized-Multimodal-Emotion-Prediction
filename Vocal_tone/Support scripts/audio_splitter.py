from pydub import AudioSegment
import wave
import os

def split_audio(input_file, output_dir, start_time, segments_no):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Calculate the total duration of the audio in milliseconds
    total_duration_ms = len(audio)

    interval_ms = total_duration_ms / segments_no

    # Create the output directory if it doesn't existc
    os.makedirs(output_dir, exist_ok=True)
    start = start_time
    end = start_time + interval_ms
    i = 127
    # Split the audio into intervals and save them
    while (end<=total_duration_ms):
        interval = audio[start:end]

        # Generate output file name
        output_file = os.path.join(output_dir, f"Cleaned_angry_{i}.m4a")

        # Export the interval as WAV file
        interval.export(output_file, format="wav")
        start = end
        end = end + interval_ms
        i = i+1
        

    print("Audio split into intervals successfully.")

# Example usage
input_file = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Vocal\Original\\angry2.m4a"  # Provide the path to your input audio file
output_dir = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Vocal\Original"  # Output directory to save intervals

split_audio(input_file, output_dir, 0, 2)
