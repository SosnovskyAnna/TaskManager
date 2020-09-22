import requests
from sender import send_message
from receiver import recieve_message
from auth import authenticate

def client():
    got_message = 0
    authenicated = False

    while(authenicated == False):
        name = input("Введите имя:")
        password = input("Введите пароль:")
        reply = authenticate(name, password)
        authenicated = reply.json()["reply"]

    print("name", name)
    print("pass", password)



    while(True):
        print("\n\n")
        command = input('Введите команду(send - для отправки сообщения, get - для получения новых)')
        if command == 'send':
            text = input("Введите сообщение:")
            send_message(name, text)
        elif command == 'get':
            data = recieve_message(got_message)
            messages = data["messages"]
            print(messages)
            last_message = messages.pop()
            got_message = last_message["id"]
        else:
            print("Команда не найдена")
    return

client()