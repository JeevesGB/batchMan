import os
import subprocess

FFMPEG_PATH = r"ffmpeg/ffmpeg.exe"
INPUT_FOLDER = "mp3"
OUTPUT_FOLDER = "mp3/wav"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(".mp3"):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_filename = os.path.splitext(filename)[0] + ".wav"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        command = [
            FFMPEG_PATH,
            "-y",  # overwrite output files
            "-i", input_path,
            output_path
        ]

        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Conversion complete.")