import webbrowser

UPSTOX_API_KEY = 'cbc66185-898f-4059-9333-1df4dd33d767'
UPSTOX_API_SECRET = 'xhat00t1rg'
SCOPE = 'read,write'
RESPONSE_TYPE = 'code'
UPSTOX_REDIRECT_URI = 'http://localhost:8000/callback'

auth_url = f"https://api-v2.upstox.com/login?apiKey={UPSTOX_API_KEY}&redirect_uri={UPSTOX_REDIRECT_URI}&response_type={RESPONSE_TYPE}"
print("Open this URL in your browser to authorize the app:", auth_url)
webbrowser.open(auth_url)
