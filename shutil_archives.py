import shutil
import os

#----Setup: Create a dummpy dir for archive----------
data_folder = "my_data_for_archive"
os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)
with open(os.path.join(data_folder, "important.txt"), 'w') as f:
    f.write("Important data here")
with open(os.path.join(data_folder, "docs", "nodes.md"), 'w') as f:
    f.write("Meeting notes")
print(f"Created a dummy folder for archive: '{data_folder}'")

# ---Create a Zip archive----------
archive_name = "my_data_archive"
try:
    # Creates my_data_archive.zip in the current directory
    # Containing the contents of "my_data_for_archive"
    archive_path = shutil.make_archive(archive_name, 'zip', root_dir=data_folder)
    print(f"Archive created: '{archive_path}'")
    print(f"Does archive exist? {os.path.exists(archive_path)}")
except Exception as e:
    print(f"Error occured during archive: {e}")
    
