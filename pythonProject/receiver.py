import requests

def recieve_message(after_id = 0):
    url = 'http://127.0.0.1:5000/messages'

    response = requests.get(url, params={'after_id': after_id})
    return response.json()