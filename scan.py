import os 

root_dir = r"sound"

output_file = "list.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for foldername, subfolders, filenames in os.walk(root_dir):
        if filenames:
            f.write(f"[{foldername}]\n")
            for file in filenames:
                f.write(f"[{file}]\n")
            f.write("\n")

print("File Scanned.")
