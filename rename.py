import os
import shutil

list_file = "list.txt"
source_dir = r"wav_pool"      # your random .wav files
output_root = r"hl_sound"     # final structured output

targets = []
current_folder = None

with open(list_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        # Folder line
        if line.startswith("[") and "\\" in line:
            current_folder = line.strip("[]")

        # File line
        elif line.startswith("[") and line.endswith("]"):
            filename = line.strip("[]")
            targets.append((current_folder, filename))

source_files = [
    f for f in os.listdir(source_dir)
    if f.lower().endswith(".wav")
]

source_files.sort()  

if len(source_files) < len(targets):
    raise Exception(f"Not enough .wav files ({len(source_files)}) for targets ({len(targets)})")

for i, (folder, new_name) in enumerate(targets):
    src_path = os.path.join(source_dir, source_files[i])

    dest_folder = os.path.join(output_root, folder)
    os.makedirs(dest_folder, exist_ok=True)

    dest_path = os.path.join(dest_folder, new_name)

    shutil.move(src_path, dest_path)  
    
print("All files processed successfully.")