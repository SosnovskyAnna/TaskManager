import requests

def send_message(name, text):
    url = 'http://127.0.0.1:5000/send'

    data = {
        'name': name,
        'text': text
    }

    response = requests.post(url, json=data)
    #print(response.status_code)
    #print(response.json())
    return True