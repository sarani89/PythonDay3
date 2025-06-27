import pathlib
import os

# -------1. Creating paath Objects ---------

# Current working directory
print(pathlib.Path)
#print(os.get.cwd('.'))
current_dir = pathlib.Path.cwd()
print(f"Current working directory (path object): {current_dir}")

# A relative path
relative_path = pathlib.Path('my_document.txt')
print(f"Relative file path: {relative_path}")

# An absolute path  (example, adjust for your OS)
absolute_path = relative_path.resolve()
print(f"Absolute file path: {absolute_path}")

# Joining Paths using the / operator (very intuitive!)
joined_path = current_dir / 'data' / 'reports' / 'report.csv'
print(f"Joined path using / operator: {joined_path}")


# ----- 2. Accessing path componenets------\
print(f"Full path: {joined_path}")
print(f"File/Folder name: {joined_path.name}")  # report.csv
print(f"Parent directory: {joined_path.parent}")    # C:\Users\Student_15\Desktop\PythonDay3\data\reports
print(f"File stem (name without suffix): {joined_path.stem}")   # report
print(f"File suffix (extension): {joined_path.suffix}")     # .csv
print(f"All suffixes: {joined_path.suffixes}")  #[.csv]
print(f"Anchor (root of the path): {joined_path.anchor}")   #  C:\
print(f"Path parts: {joined_path.parts}")   # ('C:\\', 'Users', 'Student_15', 'Desktop', 'PythonDay3', 'data', 'reports', 'report.csv')