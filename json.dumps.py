# Python program to convert 
# Python object to JSON
	
import json 
	
# Data to be written 
dictionary ={ 
"id": "04", 
"name": "Pasha", 
"department": "HR"
} 
	
# Serializing json 
json_object = json.dumps(dictionary, indent = 4) 
print(json_object)


# json.dumps() method can convert a Python object into a JSON string.

# Syntax: json.dumps(dict, indent) 
# dictionary – name of dictionary which should be converted to JSON object.
# indent – defines the number of units for indentation
