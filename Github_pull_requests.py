import requests

#/repos/{owner}/{repo}/pulls

#"https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(response)

#print(response.json())

details = response.json()

for i in range(len(details)):
    print(details[i]["user"]["login"]) # user/login-- just like parsing down the dir
    
    
    





