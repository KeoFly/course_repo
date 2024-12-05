import json


def register(login, password):
    with open("Task1-3_info.json", "r") as f:
        info = json.load(f)
    if login not in info.keys():
        info[login] = password
        with open("Task1-3_info.json", "w") as f:
            json.dump(info, f)
    else:
        print("Такой логин уже существует!")

def login_function(login, password):
    with open("Task1-3_info.json", "r") as f:
        info = json.load(f)
    if login in info.keys():
        if info[login] == str(password):
            print("Успешный вход в систему!")
        else:
            print("Пароль неверный.")

while True:
    q1 = input("Вход, регистрация или выход? ")
    if q1.lower() == "выход":
        break
    elif q1.lower() == "вход":
        login = input("Введите логин ")
        password = input("Введите пароль ")
        login_function(login, password)
    elif q1.lower() == "регистрация":
        login = input("Введите логин ")
        password = input("Введите пароль ")
        register(login, password)
    else:
        print("Я вас не понял, введите одну из команд (вход, регистрация выход).")