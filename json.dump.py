# json.dump() method can be used for writing to JSON file.

# Syntax: json.dump(dict, file_pointer) 
# dictionary – name of dictionary which should be converted to JSON object.
# file pointer – pointer of the file opened in write or append mode.


# Python program to write JSON to a file


import json

# Data to be written
dictionary ={
	"name" : "sathiyajith",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}

with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile)
