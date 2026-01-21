import os
from PIL import Image, UnidentifiedImageError

def clean_corrupted_images(folder_path):
    deleted = 0
    total = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                total += 1
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        img.verify()
                except (IOError, SyntaxError, UnidentifiedImageError):
                    print(f"Removing corrupted image: {file_path}")
                    os.remove(file_path)
                    deleted += 1

    print(f"\n✅ Scan complete: {deleted} corrupted out of {total} total images removed.")

# List of dataset folders to scan
folders = [
    "data_split/train",
    "data_split/val",
    "data_split/test"
]

for folder in folders:
    if os.path.exists(folder):
        print(f"\n🧹 Cleaning folder: {folder}")
        clean_corrupted_images(folder)
    else:
        print(f"⚠️ Folder not found: {folder}")