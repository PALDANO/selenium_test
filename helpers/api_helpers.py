import requests

def login_and_get_token(username, password):
    url = "https://playerauthentication-at.greentube.com/gametwist.widgets.web.site/de/api/login-v1"
    payload = {"nickname": username, "password": password, "autoLogin": True}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["accessToken"]

def get_balance(token):
    url = "https://www.gametwist.com/nrgs/de/api/userstate-v1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["balance"]["funMoney"] / 1000
