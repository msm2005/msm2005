import time
from termcolor import colored
import random
import os



def __main__():
	cls()
	logo()
	print()
	login()


def cls():
	os.system('cls')



def logo():
    print("""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
""")

def login():
	root_sign_un = input('C&C Username: ')
	if root_sign_un != 'sysadmin':
		cls()
		print(colored('WRONG USERNAME TERMINATING PROGRAM!!!', 'red'))
		time.sleep(3)
		exit()
	cls()
	logo()
	print()
	print(colored('C&C Username: ' + root_sign_un, 'green'))
	root_sign_pass = input('C&C Password: ')
	if root_sign_pass != 'sysadmin123':
		cls()
		print(colored('WRONG PASSWORD TERMINATING PROGRAM!!!', 'red'))
		time.sleep(3)
		exit()
	cls()
	logo()
	print()
	print(colored('C&C Username: ' + root_sign_un, 'green'))
	print(colored('C&C Password: ' + root_sign_pass, 'green'))
	time.sleep(3)
	cls()

__main__()