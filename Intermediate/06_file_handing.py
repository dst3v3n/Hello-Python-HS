### File Handling ###

import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+")

txt_file.write("Mi nombre es Harold\nMi apellido es Sabogal\n18 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Java")
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

read_file = open ("Intermediate/my_file.txt", "r+")
for line in read_file.readlines():
    print(line)

# os.remove("Intermediate/my_file.txt")

# .json file 

import json

json_file = open ("Intermediate/my_file.json", "w+")

json_test = {
            "name" : "Harold", 
            "surname" : "Sabogal", 
            "age" : 18, 
            "language" : ["Python", "java" , "javaScript"],
            "website" : "harold"
            }

json.dump (json_test,json_file, indent = 2)

json_file.close ()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load (open ("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file
 
import csv

csv_file = open ("Intermediate/my_file.csv", "w+")

csv_write = csv.writer(csv_file)
csv_write.writerow(["name" , "surname" , "age" , "lenguage" , "website"])
csv_write.writerow(["Harold" , "Sabogal" , 18 , "python" , "Steven"])
csv_write.writerow(["Roswell" , "" , 2 , "COBOL" , ""])

csv_file.close ()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file

import xlrd 

# .xml file  

import xml