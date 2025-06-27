import shutil
import os

# ----Setup: Create a dummy file and a target directory -----
file_to_move = "report.pdf"
target_dir = "archives"

with open(file_to_move, 'w') as f:
    f.write("Confidential report")
os.makedirs(target_dir, exist_ok=True)
print(f"Created '{file_to_move}' and '{target_dir}'")

try:
    shutil.move(file_to_move, target_dir)
    print(f"New path : {os.path.join(target_dir, file_to_move)} ")
except FileNotFoundError:
    print(f"Source File '{file_to_move}' not found ")
except Exception as e:
    print(f"An error occured: {e}")