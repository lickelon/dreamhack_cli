import requests
import json
import zipfile
import os

class Wargame:
    def __init__(self, id):
        self.id = id
        self.url = "https://dreamhack.io/api/v1/wargame/challenges/" + str(self.id)
    
    def fetch(self, session):
        #print(f"Fetch Wargame", end=' ')
        response = session.get(self.url)
        if response.status_code == 200:
            self.json = json.loads(response.text)
            self.title = self.json['title']
            self.link = self.json['public']
            #print(f"Success! - {self.title}")
        else:
            print(f"Failed with error: {response.status_code}")
    
    def download(self):
        #print(f"Download Wargame({self.title})", end=' ')
        self.file_name = str(self.id)+'.zip'
        try:
            with open(self.file_name, "wb") as file:
                response = requests.get(self.link)
                if response.status_code == 200:
                    file.write(response.content)
                    #print(f"Success! - {self.file_name}")
                else:
                    print(f"Failed with error: {response.status_code}")
        except:
            print("\nCan't make zip-file")

    def unzip(self, path='./'):
        #print(f"Unzip Wargame", end=' ')
        try:
            with zipfile.ZipFile(self.file_name) as zip_file:
                self.path = f'{path}DH{self.id}_{self.title}'
                zip_file.extractall(path=self.path)
            #print(f'Success! - {self.path}')
            os.remove(self.file_name)
            #print("zip-file removed")
        except zipfile.error:
            print("Can't unzip zip-file")
        except os.error:
            print("Can't remove zip-file")