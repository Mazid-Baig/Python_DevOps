from flask import Flask

import requests
from requests.auth import HTTPBasicAuth

import json

app = Flask(__name__)


# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https:/XXXXXXXX.atlassian.net//rest/api/3/issue"

    API_TOKEN = "XXXXXXXXXX"

    auth = HTTPBasicAuth("XXXXXX@gmail.com", API_TOKEN)

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
                            "text": "Order entry fails when selecting supplier.",
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
        },
        "summary": "Main order flow broken",
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
    
#     webhook = request.json
#     response = None
#     if webhook['comment'].get('body') == "/jira":
#         response = requests.request("POST", url, data=payload, headers=headers, auth=auth)
#         return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
#     else:
#         print('Jira issue will be created if comment include /jira')

#     return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)