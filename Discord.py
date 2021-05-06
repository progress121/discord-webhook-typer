from dhooks import Webhook
import time
time.sleep(0.9)
print("Simple Discord webhook Typer v1.0")
time.sleep(0.5)

url = input("Enter your Webhook here: ")
webhook_url = Webhook(url)

discord_msg = input("Enter your Message here: ")

webhook_url.send(discord_msg)

