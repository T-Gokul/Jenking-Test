import requests
from datetime import datetime

def get_token_expiration(token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get('https://api.github.com/user', headers=headers)

    if response.status_code == 200:
        token_info = response.json()
        expires_at_str = token_info.get('updated_at')

        updated_at = datetime.strptime(expires_at_str, "%Y-%m-%dT%H:%M:%SZ")
        now = datetime.now()
        result = now - updated_at
        result = result.days       
        if result == 7:
            print("Token is going to expire, renew it")
        else:
            print(f"Token will expire in {result} days")

    else:
        return f"Error: {response.status_code}, {response.text}"

get_token_expiration('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')
