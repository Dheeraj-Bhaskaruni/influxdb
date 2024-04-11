import requests
import json

# Replace these variables with your actual InfluxDB details
influx_url = "http://localhost:8086"
org = "automation"
bucket = "auto"
token = "gUuX82zqjm9gzSF91FURPTiJjA2fZ2x6FarALLfPFS9GEZhSM97XnARSpW37I_Jihj1YHikIzdyJ3rSd0V2C2A=="  # An existing token with permissions to create new tokens

headers = {
    "Authorization": f"Token {token}",
    "Content-type": "application/json",
}

data = {
    "description": "New API Token",
    "permissions": [
        {
            "action": "read",
            "resource": {
                "type": "buckets",
                "name": bucket,
                "org": org,
            },
        },
        {
            "action": "write",
            "resource": {
                "type": "buckets",
                "name": bucket,
                "org": org,
            },
        },
    ],
}

response = requests.post(f"{influx_url}/api/v2/authorizations", headers=headers, data=json.dumps(data))

if response.status_code == 201:
    new_token = response.json()['token']
    print(f"New Token: {new_token}")
else:
    print(f"Failed to create token: {response.text}")
