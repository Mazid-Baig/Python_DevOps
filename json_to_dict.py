# Import JSON module
import json

# Define JSON string
jsonString = '{ "id": 121, "name": "Mazid", "course": "MERN Stack"}'

# Convert JSON String to Python
student_details = json.loads(jsonString)

# Print Dictionary
print(student_details)

print(type(jsonString))

print(type(student_details))

# Print values using keys
print(student_details['name'])
print(student_details['course'])

# The keys in JSON can be only strings where as the keys in the dictionary can be any hashable object.
# In JSON, the keys are sequentially ordered and can be repeated where as in the dictionary, the keys cannot be repeated and must be distinct.