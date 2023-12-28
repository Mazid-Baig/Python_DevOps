import json

person_details = '{"name" : "Mazid, "age" : 29, "Gender" : "Male" }'

print(type(person_details))

details = json.loads(person_details)

print(type(details))

print(details["age"])

#So load is for a file, loads for a string