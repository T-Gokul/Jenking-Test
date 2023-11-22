import requests
from datetime import datetime
print("Testing")
token = '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'
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get('https://api.github.com/user', headers=headers)

token_info = response.json()
expires_at_str = token_info.get('updated_at')

updated_at = datetime.strptime(str(expires_at_str), "%Y-%m-%dT%H:%M:%SZ")
now = datetime.now()
result = now - updated_at
result = result.days       
if result == 7:
    print("Token is going to expire, renew it")
else:
    print(f"Token will expire in {result} days")

# get_token_expiration('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')
