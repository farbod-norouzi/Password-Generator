# Start (Import libraries)

import os
from os import system
import platform 
import sys
import datetime
import random
try:
    from tqdm import tqdm
    from colorama import Fore 
except:
    print("Installing prerequisites")
    system("pip install tqdm")
    system("pip install colorama")
    exit('\n',"Run script Again")

# End (Import libraries)

# Start (Banner & Clearing)

def clear():
   result = platform.uname()[0]
   if result == "Windows":
      system("cls")
   elif result == "Linux":
      system("clear")
clear()

print(Fore.RED+ """ ___                                                 _ 
(  _`\                                              ( )
| |_) )  _ _   ___   ___  _   _   _    _    _ __   _| |
| ,__/'/'_` )/',__)/',__)( ) ( ) ( ) /'_`\ ( '__)/'_` |
| |   ( (_| |\__, \\__, \| \_/ \_/ |( (_) )| |  ( (_| |
(_)   `\__,_)(____/(____/`\___x___/'`\___/'(_)  `\__,_)
                                                       
                                                       """+Fore.RESET)

# Start (Banner & Clearing)

# Start (APP & Get Input From User)

print(" Welcome To Password Generator ... ",'\n')
try:
    pass_range = int(input('Please Enter The Password Range : '))
except:
    print(Fore.RED+ "You canceled the program!"+Fore.RESET)
    sys.exit()

# Start (Progress bar)
finish = "\n \n Keep Safe it! \n"
print("Please Wait...",'\n')

for i in tqdm(range(pass_range)):

    pass

# End (Progress bar)

# Start (Make You're Password)

print('\n',"You're Password is:",'\n')
alefba = ("abcdefglomnp123456789_*#$@!%ASDFGHJKLMNBVCXZQWERTYUIOP")
if pass_range >= 8:
    for i in range(pass_range):
        i = random.choice(alefba)
        print(i, end= '')
    print(finish)     
else:
    print('You Can Not Choice >8 Number !')

# End (Make You're Password)

# Start (APP & Get Input From User)