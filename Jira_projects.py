# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json


# url = "https://your-domain.atlassian.net/rest/api/3/project"

# auth = HTTPBasicAuth("email@example.com", "<api_token>")


url = "https://XXXXX.atlassian.net//rest/api/3/project"

auth = HTTPBasicAuth ("xxxx@gmail.com", "API_TOKEN")
headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# when we want to parse the json inforamtion we need to convert the json to dictionary and execute operations on dictionary.

output = json.loads(response.text)

name = output[0]["name"]
print(name)

#response.text returns the content of the response, in unicode. Basically, it refers to Binary Response content. Python requests are generally used to fetch the content from a particular resource URI. Whenever we make a request to a specified URI through Python, it returns a response object. Now, this response object would be used to access certain features such as content, headers, etc. This  revolves around how to check the response.text out of a response object. 
