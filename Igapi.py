import requests

def follow_user(username, access_token):
    url = f"https://api.instagram.com/v1/users/search?q={username}&access_token={access_token}"
    response = requests.get(url)
    data = response.json()

    if data['meta']['code'] == 200:
        user_id = data['data'][0]['id']
        url = f"https://api.instagram.com/v1/users/{user_id}/relationship?access_token={access_token}"
        payload = {"action": "follow"}
        response = requests.post(url, data=payload)

        if response.status_code ==