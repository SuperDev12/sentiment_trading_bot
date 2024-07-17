import requests

UPSTOX_API_KEY = 'cbc66185-898f-4059-9333-1df4dd33d767'
UPSTOX_API_SECRET = 'xhat00t1rg'
REDIRECT_URI = 'http://localhost:8000/callback'
GRANT_TYPE = 'authorization_code'

# Enter the authorization code you received after authorizing the app
authorization_code = input("Enter the authorization code: ")

token_url = "https://api-v2.upstox.com/login/authorize"
payload = {
    'apiKey': UPSTOX_API_KEY,
    'apiSecret': UPSTOX_API_SECRET,
    'redirect_uri': REDIRECT_URI,
    'code': authorization_code,
    'grant_type': GRANT_TYPE
}

response = requests.post(token_url, data=payload)
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    print("Access Token:", access_token)
    
    # Save the access token for future use
    with open("access_token.txt", "w") as f:
        f.write(access_token)
else:
    print("Failed to retrieve access token:", response.text)
