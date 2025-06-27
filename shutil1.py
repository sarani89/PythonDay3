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


# -----Setup: Create a dummy source directory tree------------
src_dir = "My_new_proj"
os.makedirs(os.path.join(src_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(src_dir, "js"), exist_ok=True)
with open(os.path.join(src_dir, "index.html"), 'w') as f:
    f.write("<html></html>")
with open(os.path.join(src_dir, "css", "style.css"), 'w') as f:
    f.write("body{}")
print(f"Created dummy source directory: '{src_dir}'")


# ----Copy the directory tree----------
dest_dir = "my_backup_proj"
try:
    # If dest dir already exist and is not empty, copytree will raise an error
    # To overwrite, you'd typically remove the destination first or handle 
    shutil.copytree(src_dir, dest_dir)
    print(f"'{src_dir}' copied to '{dest_dir}' successfully")
    print(f"Contents of the destination dir:")
    for root, dirs, files in os.walk(dest_dir):
        level = root.replace(dest_dir, '').count(os.sep)
        indent = ' '*4*(level + 1)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' '*4*(level + 1)
        for f in files:
                print(f"{subindent}{f}")  # Print 4 indents and  the file name
except FileExistsError:
    print(f"Error: Destination directory '{dest_dir}' already exist")
except Exception as e:
    print(f"Error occured during copytree: {e}")


#----Crean-----------
if os.path.exists(src_dir):
    shutil.rmtree(src_dir)
if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)
print("Cleaned my dummy directories.")



# ---Create a dummy file-------
src_file = "src_doc.txt"
with open(src_file, 'w') as f:
    f.write("This is the original content")
print(f"Created '{src_file}' for copying")

# -----Copy file------------
dst_file = "dst_doc.txt"
try:
    shutil.copy(src_file, dst_file)
    print(f"'{src_file}' copied to '{dst_file}' successfully")
    print(f"Content of '{dst_file}': {open(dst_file).read()}")
except FileNotFoundError:
    print(f"Error: source file '{src_file}' not found")
except Exception as e:
    print(f"Eror found. {e}")

#------Cleanup----------

if os.path.exists(src_file):
    os.remove(src_file)
if os.path.exists(dst_file):
    os.remove(dst_file)
print("Cleanup completed for dummy files.")

