import os
import shutil
import random

# Paths
original_data_path = "data/"
output_path = "data_split/"
classes = ['wildfire', 'no_wildfire']

# Split percentages
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create new folders
for split in ['train', 'val', 'test']:
    for cls in classes:
        os.makedirs(os.path.join(output_path, split, cls), exist_ok=True)

# Function to split and copy
for cls in classes:
    source_folder = os.path.join(original_data_path, cls)
    images = os.listdir(source_folder)
    random.shuffle(images)

    total = len(images)
    train_end = int(train_ratio * total)
    val_end = train_end + int(val_ratio * total)

    for i, img in enumerate(images):
        src = os.path.join(source_folder, img)
        if i < train_end:
            dst = os.path.join(output_path, 'train', cls, img)
        elif i < val_end:
            dst = os.path.join(output_path, 'val', cls, img)
        else:
            dst = os.path.join(output_path, 'test', cls, img)
        shutil.copyfile(src, dst)

print("✅ Dataset split into train/val/test under 'data_split/'")
