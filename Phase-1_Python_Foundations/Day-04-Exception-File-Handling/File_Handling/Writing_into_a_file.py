
with open("Phase-1_Python_Foundations/Day-04-Exception-File-Handling/File_Handling/data.csv","w") as file:
    file.write("Yadagiri")
    file.write("Payal")
    file.write("Joe")

with open("Phase-1_Python_Foundations/Day-04-Exception-File-Handling/File_Handling/data.csv","r") as file1:
    for lines in file1:
        print(lines)
