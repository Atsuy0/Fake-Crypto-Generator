import string, random
from discord_webhook import DiscordWebhook

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

print(main+ending+n)

