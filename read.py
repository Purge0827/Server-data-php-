#Coded by Purge#1338
import os
from os import system
import requests
import time
from time import sleep

print("server_data.php Reader")
print("Coded by Purge#1338")
os.system("color 1")
os.system("color 2")
os.system("color 3")
os.system("color 4")
os.system("color 5")
os.system("color 6")
os.system("color 7")
os.system("color 8")
os.system("color 9")
os.system("color A")
os.system("color B")
os.system("color C")
os.system("color D")
os.system("color 9")
ip = input('IP Address > ')
print("Succesfully readed, please wait 5 seconds.....")
post = requests.post(f'http://{ip}/growtopia/server_data.php')
sleep(5)
print('Target server_data.php : ')
print('\n')
print(post.text)
print("\nReaded!")
sleep(10)