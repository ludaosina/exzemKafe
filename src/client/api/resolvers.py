import requests


def check_login(login: str, password: str):
    data = f'{{ "login": "{login}", "password": "{password}" }}'
    answer = requests.get(url='http://127.0.0.1:8000/users/login/', data=data).json()
    code = answer["code"]
    msg = answer["message"]
    if code != 200:
        return f"Server error: {msg}"
    elif code == 200:
        return answer["post_id"][0]
