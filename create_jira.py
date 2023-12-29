# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://XXXXXX.atlassian.net//rest/api/3/issue"

API_TOKEN = "XXXXX"
auth = HTTPBasicAuth("XXXXX@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": " Python event jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "BAIG"
    },
    "issuetype": {
      "id": "10003"
      #issue type id is for bug, selected from url of jira dashboard
    },
    "summary": "Python event based JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))