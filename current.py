import os

# Define the directory you want to change to
# Make sure this directory exists on your system

new_directory = ".\\temp"  # Example for Linux/macOS "./tmp"
# for windows, it might be something like "C:\\Users\\YourUser\\Documents"

print("Current working directory:", os.getcwd())

if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory)
    print(f"Changed directory to: {os.getcwd()}")
else:
    print(f"Directory '{new_directory}' does not exist or is not a directory")



# print a dir path and a file name
file_path = ".\\temp\\file.txt"

directory_name = os.path.dirname(file_path)
basename = os.path.basename(file_path)

print(f"Directory name: {directory_name}")
print(f"Base name: {basename}")


# Create a new file named test.txt and Write Hellow in it

dirA = "C:\\Users\\Student_15\\Desktop\\PythonDay3"
fileA = ".\\test.txt"
print(f"Dir path: {new_directory}")

with open(fileA, 'w') as f:
    f.write("Hello")

os.makedirs(dirA, exist_ok=True)

if os.path.exists(fileA):
    print(f"'{dirA}' exists")
else:
    print(f"'{fileA}' does not exist")

if os.path.exists(dirA):
    print(f"'{dirA}' exists")
else:
    print(f"'{dirA}' does not exist")



### New

path1 = ".\\temp\\test.txt"
path2 = ".\\temp"    
path3 = "non_existent path"

print(f"'{path1}' is a file: {os.path.isfile(path1)}")
print(f"'{path1}' is a directory: {os.path.isdir(path1)}")

print(f"'{path2}' is a file: {os.path.isfile(path2)}")
print(f"'{path2}' is a directory: {os.path.isdir(path2)}")

print(f"'{path3}' is a file: {os.path.isfile(path3)}")
print(f"'{path3}' is a directory: {os.path.isdir(path3)}")


