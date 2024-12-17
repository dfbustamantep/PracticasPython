## File handing 
import os
# .txt

#txt_file=open("Intermediate/my_file.txt","r+") # Leer y escribir
txt_file=open("Intermediate/my_file.txt","r") 
#txt_file.write("Mi nombre es Daniel\nMi apellido es Bustamante\n20 años\nY mi lenguaje favorito es Python")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)
    
#txt_file.write("\nAunque tambien me gusta C++")
print(txt_file.readline())

txt_file.close()
#os.remove("Intermediate/my_file.txt")

#.JSON
import json
json_file =open("Intermediate/my_file.json","w+")

json_text ={
    "name":"Daniel",
    "surname":"Bustamante",
    "age":20,
    "lenguages":["Python","Java","C++"],
    "website":"https://github.com/dfbustamantep"
}

json.dump(json_text,json_file,indent=4)
json_file.close()

with open("Intermediate/my_file.json")as my_other_file:
    for line in my_other_file.readlines():
        print(line)
    
json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

#.csv
import csv

csv_file=open("Intermediate/my_file.csv","w+")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","languege","website"])
csv_writer.writerow(["Daniel","Bustamante","20","Python","https://github.com/dfbustamantep"])

csv_file.close()

with open("Intermediate/my_file.csv")as my_other_file:
    for line in my_other_file.readlines():
        print(line)
#.xlsx
#.xml
import xml