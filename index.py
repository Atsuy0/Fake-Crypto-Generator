import string, random
from discord_webhook import DiscordWebhook
import os
import time
from colorama import Back, Fore, Style, deinit, init

os.system('cls')

print(" ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ") 
print("██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
print("██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝")
print("██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║       ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
print("╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║")
print(" ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
print("                     Developped by Atsuyo")
init()

print("\nVeillez entrez votre webhook :")
print("\nUser" +Fore.CYAN + "$" +Fore.WHITE , end='')
launch = input()

deinit()


chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)

launch =""

main = "``[-]`` "

n = " - 0.0000 ETH"

for i in range(1):
    ending = ""
    for i in range(random.randint(52,52)):
        ending += random.choice(chars)

webhook = DiscordWebhook(url=launch, content=main+ending+n)
response = webhook.execute()

