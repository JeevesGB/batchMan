import os
import shutil

list_file = "tstlist.txt"
source_dir = r"mp3/wav"       # your random .wav files
output_root = r"hl_sound"      # final structured output

targets = []
current_folder = None

# Read list.txt
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
            if filename.lower().endswith(".wav"):  # only .wav targets
                folder = current_folder if current_folder else "default"
                # Optional: remove leading 'sound\' if present
                if folder.lower().startswith("sound\\"):
                    folder = folder[6:]
                targets.append((folder, filename))

# Get source files in sorted order
source_files = sorted([
    f for f in os.listdir(source_dir)
    if f.lower().endswith(".wav")
])

if not source_files:
    print("No .wav files found in source_dir!")
else:
    print(f"Found {len(source_files)} .wav files. Mapping to {len(targets)} targets.")

# Map source files to targets using zip (stops at shortest list)
for (folder, new_name), src_file in zip(targets, source_files):
    src_path = os.path.join(source_dir, src_file)
    dest_folder = os.path.join(output_root, folder)
    os.makedirs(dest_folder, exist_ok=True)
    dest_path = os.path.join(dest_folder, new_name)

    shutil.move(src_path, dest_path)
    print(f"{src_file} → {os.path.join(folder, new_name)}")

print("All available files processed successfully.")