# ======================>>>>>>>>  CSV file  <<<<<<<<<<================

import csv
with open("/Users/sahildevli/Documents/python/BasicPythonSyntax/diets.csv", 'r') as file1:
    reader = csv.reader(file1)
    next(reader)  # skip header
    for row in reader:
        print(row)



# ================>>>>>>>>>>>  TEXT FILE <<<<<<<<<=======================

# for .txt file in python

file = open("/Users/sahildevli/Documents/python/BasicPythonSyntax/abc.txt", 'r')
contect = file.readlines()
for line in contect:
    print(line.strip())

# write mode cleare the present data of text file and write new content provide to writter
# with open("/Users/sahildevli/Documents/python/BasicPythonSyntax/abc.txt", 'w') as fileWriter: 
#     fileWriter.write("This is new line")
#     fileWriter.write("\nSecond line")

# to add data afte the present data in file we have to use append 'a'
with open("/Users/sahildevli/Documents/python/BasicPythonSyntax/abc.txt", 'a') as fileWriter: 
    fileWriter.write("\nappended line")