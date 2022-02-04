import requests
import json

def get_license(api_key: str, license_key: str):
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    req = requests.get(f'https://api.hyper.co/v6/licenses/{license_key.strip()}', headers=headers)
    if req.status_code == 200:
        return json.loads(req.text)
    return None

def update_license(api_key: str, license_key: str, hardware_id: str):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'metadata': {
            'hwid': hardware_id
        }
    }
    
    req = requests.patch(
        f'https://api.hyper.co/v5/licenses/{license_key.strip()}',
        headers=headers,
        json=payload
    )
    if req.status_code == 200:
        return True
    return None