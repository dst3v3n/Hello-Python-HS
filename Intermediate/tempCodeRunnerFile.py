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
