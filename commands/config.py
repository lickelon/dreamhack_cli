import json
import sys
from classes.user import User

def config():
    if len(sys.argv) == 2:
        try:
            with open("user_info.json", "r") as file:
                data = json.load(file)
                print_info(data)
        except FileNotFoundError:
            get_input()
    elif len(sys.argv) == 3 and sys.argv[2] == '-m':
        get_input()
    else:
        print("Usage : dh config (-m)")

def get_input():
    email = input(" email : ")
    password = input(" password : ")
    data = {
        "email" : email,
        "password" : password
    }
    print_info(data)
    with open("user_info.json", "w") as file:
        json.dump(data, file)
    User().login()

def print_info(data):
    print(f"email : {data['email']}")
    print(f"password : {'*'*len(data['password'])}")