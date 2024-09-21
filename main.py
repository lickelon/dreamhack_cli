import sys
from commands.config import config
from commands.create import create
from commands.help import help

if __name__ == '__main__':
    if sys.argv[1] == 'config':
        pass
    if sys.argv[1] == 'create':
        create()
    if sys.argv[1] == 'help' or len(sys.argv) == 1:
        help()