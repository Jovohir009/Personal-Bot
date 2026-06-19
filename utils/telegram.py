import requests


def telegram_request(token, method, payload):
    response = requests.post(
        f"https://api.telegram.org/bot{token}/{method}", json=payload
    )

    return response.json()
