from classes.user import User
from classes.wargame import Wargame
import sys

def create():
    user = User()
    user.login()
    if len(sys.argv) != 3:
        print("Usage : dh create <wargame_link|wargame_id>")
        return
    id = int(''.join([num for num in sys.argv[2] if num.isdigit()]))
    wargame = Wargame(id)
    wargame.fetch(user.session)
    wargame.download()
    wargame.unzip()