from flask import Flask, request
import time

app = Flask(__name__)
db = []


@app.route("/")
def hello():
    return """"First page! 
    <a href='/status'>Status!</a>
    <a href='/counter'>Counter!</a>
    """

users = dict()

@app.route("/auth", methods=['GET', 'POST'])
def auth():
    data = request.json
    name = data['name']
    password = data['password']
    if users.get(name) == None:
        users[name] = password
        return {"reply": True}
    elif users.get(name) == password:
        return {"reply": True}
    else:
        return {"reply": False}


@app.route("/status")
def status():
    my_time = time.asctime()
    return {
        'status': True,
        'name': "Pigeon",
        'time': my_time,
        'users': len(users)
        }


@app.route("/send", methods=['GET', 'POST'])
def send():
    data = request.json

    timestamp = time.asctime()
    db.append({
        'id': len(db),
        'name': data['name'],
        'text': data['text'],
        'timestamp': timestamp
    })
    return {'ok':True}

@app.route("/messages")
def messages():
    if 'after_id' in request.args:
        after_id = int(request.args['after_id'])
    else:
        after_id = 0
    return {'messages':db[after_id:]}


app.run()
