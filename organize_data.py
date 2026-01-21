import os
import shutil

# Source folders (update path if needed)
base_path = r"C:\Users\RENUKA\Desktop\wildfire_project\data\test"
wildfire_src = os.path.join(base_path, "wildfire")
nowildfire_src = os.path.join(base_path, "nowildfire")

# Target folders
data_dir = r"C:\Users\RENUKA\Desktop\wildfire_project\data"
wildfire_dst = os.path.join(data_dir, "wildfire")
no_wildfire_dst = os.path.join(data_dir, "no_wildfire")

# Create target folders if they don't exist
os.makedirs(wildfire_dst, exist_ok=True)
os.makedirs(no_wildfire_dst, exist_ok=True)

# Move wildfire images
for filename in os.listdir(wildfire_src):
    src_file = os.path.join(wildfire_src, filename)
    dst_file = os.path.join(wildfire_dst, filename)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)

# Move no_wildfire images
for filename in os.listdir(nowildfire_src):
    src_file = os.path.join(nowildfire_src, filename)
    dst_file = os.path.join(no_wildfire_dst, filename)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)

print("✅ Dataset organized successfully!")
