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