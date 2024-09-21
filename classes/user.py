import requests
import json

class User:
    def __init__(self):
        self.url = "https://dreamhack.io/api/v1/auth/login/"
        self.session = requests.Session()
    def get_info(self):
        #TODO : user_info.json이 없으면 직접 입력 or config 안내 메세지 출력
        with open("user_info.json", "r") as file:
            data = json.load(file)
        self.email = data['email']
        self.password = data['password']
        pass
    def login(self):
        self.get_info()
        #print("Login on Dreamhack...")
        payload = {
            "email": self.email,
            "password": self.password
        }
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36"
        }

        response = self.session.post(self.url, json=payload, headers=headers)
        if response.status_code == 200:
            print("Login Success!")
            return True
        else:
            print(f"Login Failed! ERROR: {response.status_code}")
            return False