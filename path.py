import os

path_comp1 = "C:\\Users\\Student_15\\Desktop\\PythonDay3"
path_comp2 = "temp"
file_name = "monthly_report.pdf"


full_path = os.path.join(path_comp1, path_comp2, file_name)
print(full_path)

# List contents of the current direcctory
print("Contents of current directory: ")
for item in os.listdir('.'):
    print(item)

# You can also specify a path
# For example, to list contents of the /tmp directory:
#print("\nContents of /tmp dire")
#for item in os.listdir('/tmp')
    print(item)

# Create a new dir

new_dir = "my_new_dir"

try:
    os.mkdir(new_dir)
    print(f"New dir '{new_dir}'")
except FileExistsError:
    print("Dire alrady exists")
except Exception as e:
    print(f"An error occured: {e}")


# Delete a dir

NewDir = "empty_dir"
os.mkdir(NewDir) 

try:
    os.rmdir(NewDir)
    print(f"Dire '{NewDir}' removed succesfully")
except Exception as e:
    print(f"Error removing the dir '{NewDir}")


# Create and write in a file and then delte it
    
MyFile = "my_new_file"

with open(MyFile, 'w') as f:
    f.write("This is a temporary file")

try:
    os.remove(MyFile)
    print(f"The file '{MyFile}' successfully deleted")
except FileNotFoundError:
    print("File does not exist")
except Exception as e:
    print(f"An error occured: {e}")


# Rename a file
    
new_file = "my_new_fileA"
old_file = "my_old_fileA"

with open(old_file, 'w') as f:
    f.write("This is the file")

try:
    os.rename(old_file, new_file)
    print(f" The file '{old_file}' successfully renamed to '{new_file}'")
except FileNotFoundError:
    print(f"File named '{old_file}' does not exist")
except FileExistsError:
    print(f" File '{new_file}' already exist")
except Exception as e:
    print(f"Error occured: {e}")

