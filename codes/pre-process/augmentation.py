import os
from pydub import AudioSegment

def segment_audio(file_path, segment_duration_ms, overlap, output_dir):
    audio = AudioSegment.from_file(file_path, format="wav")
    length_ms = len(audio)
    start_ms = 0
    segment_number = 1

    while start_ms + segment_duration_ms <= length_ms:
        segment = audio[start_ms:start_ms + segment_duration_ms]
        segment_filename = f"{os.path.splitext(os.path.basename(file_path))[0]}_segment_{segment_number}.wav"
        segment_path = os.path.join(output_dir, segment_filename)
        segment.export(segment_path, format="wav")
        segment_number += 1
        start_ms += int(segment_duration_ms * (1 - overlap))

audio_dir = 'F:/Dipression_data/DN-BENGAL_DATA/New folder/' # Replace with the path to your audio files
output_dir = 'F:/Dipression_data/DN-BENGAL_DATA/New folder (2)/' # Replace with the path where you want to save segments
segment_duration_ms = 3000  # 3 seconds in milliseconds
overlap = 0.5  # 50% overlap

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(audio_dir):
    if filename.endswith('.wav'):
        file_path = os.path.join(audio_dir, filename)
        segment_audio(file_path, segment_duration_ms, overlap, output_dir)
