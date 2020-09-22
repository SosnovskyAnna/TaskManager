import requests

def authenticate(name, password):
    url = 'http://127.0.0.1:5000/auth'

    data = {
        'name': name,
        'password': password
    }

    response = requests.post(url, json=data)
    #print(response.status_code)
    #print(response.json())
    return response