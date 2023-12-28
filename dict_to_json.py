# import json module
import json 
	
# define Python dictionary
employee_details ={ 
"id": "04", 
"name": "sunil", 
"department": "HR"
} 
	
# Convert Python to JSON , Indent 4 is used for extra readability
json_object = json.dumps(employee_details, indent = 4) 

# Print JSON object
print(json_object) 

print(type(employee_details))

print(type(json_object))