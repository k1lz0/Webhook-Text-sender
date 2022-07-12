from time import sleep
import discord
from discord import Webhook, RequestsWebhookAdapter

print("𝙙𝙞𝙨𝙘𝙤𝙧𝙙 𝙬𝙚𝙗𝙝𝙤𝙤𝙠\n B>#3409")
choose = input("[1] Webhook Text \n[2] Embedded Webhook\n[3] Exit  \n \n>  ")

if choose == "3":
    print("Bye bye <3")
    sleep(1)
    exit()


def input_webhook_url():
    url = input("insert your webhook URL > ")

    if "https://discord.com/api/webhooks/" not in url.lower():
        print("Your webhook URL isn't correct")
        url = input_webhook_url()
    return url


webhook = input_webhook_url()

if choose == "2":
    title = input("Embed title > ")
    Desc = input("Embed description > ")
    Field1 = input("Field 1 > ")
    Field11 = input("Field 2 > ")
    Field2 = input("Field 3 > ")
    Field22 = input("Field 4 > ")
    embedVar = discord.Embed(title=title, description=Desc, color=0)
    embedVar.add_field(name=Field1, value=Field11, inline=False)
    embedVar.add_field(name=Field2, value=Field22, inline=False)
    webhook = Webhook.from_url(webhook, adapter=RequestsWebhookAdapter())
    webhook.send(embed=embedVar)
    print("< Done !")
    sleep(1)
    exit()

if choose == "1":
    text_msg = input("Type the message you want to send >")
    webhook = Webhook.from_url(webhook, adapter=RequestsWebhookAdapter())
    webhook.send(text_msg)
    print("< Done !")
    sleep(1)
    exit()
