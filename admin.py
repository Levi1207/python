import sys
from colorama import Fore, Back, Style
from colorama import init as colorama_init
from getpass import getpass
from tqdm import tqdm
import time



colorama_init(autoreset=True)
user_name = "isfandiyor"

a = input( "Enter your login: ")


def login():
    if a == user_name:
        password = getpass("Enter password: ")
        if int(password) == 1207:
            print(Fore.YELLOW + "password succsesful",("\U0001F604"))
        else:
            print("password doesn't recognized ! ",("\U0001F61C"))
            sys.exit()
        name = input("Enter you name: ")
        age = input ( "Enter yout age: ")
        if   int (age) <= 18:
            print(Fore.RED + "your age does not fit ",("\U0001F610"))
        else:
            with tqdm(total=100) as pbar:
                for i in range(10):
                    time.sleep(0.3)
                    pbar.update(10)
            print(Fore.LIGHTGREEN_EX + name + " age is " +  age ,("\U0001F606")+ Fore.LIGHTGREEN_EX +"\nYour account is succsesful ",("\U0001F60D"))
    else:
        print(Fore.RED + "You are not Admin",("\U0001F612"))
        sys.exit()


login()

