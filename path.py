import os

path_comp1 = "C:\\Users\\Student_15\\Desktop\\PythonDay3"
path_comp2 = "temp"
file_name = "monthly_report.pdf"


full_path = os.path.join(path_comp1, path_comp2, file_name)
print(full_path)