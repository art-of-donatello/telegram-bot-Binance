import json, config
from flask import Flask, request, jsonify, render_template
from binance.client import Client
from binance.enums import *
from telethon import TelegramClient, events, sync

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET)

api_id = config.API_ID
api_hash = config.API_HASH
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='Signals Global Channel'))
async def my_event_handler(event):
    print(event.raw_text) 

client.start()
client.run_until_disconnected()
 
