
with open("Phase-1_Python_Foundations/Day-04-Exception-File-Handling/File_Handling/data.csv","a") as file:
    file.write("999,Yadagiri,20,CSE,99,90,Hyd \n")

with open("Phase-1_Python_Foundations/Day-04-Exception-File-Handling/File_Handling/data.csv","r") as file1:
    for lines in file1:
        print(lines)