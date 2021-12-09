import json, config
from flask import Flask, request, jsonify, render_template
from binance.client import Client
from binance.enums import *
from telethon import TelegramClient, events, sync

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET)

api_id = config.WEBHOOK_PASSPHRASE
api_hash = config.WEBHOOK_PASSPHRASE
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='Signals Global Channel'))
async def my_event_handler(event):
    print(event.raw_text) 

client.start()
client.run_until_disconnected()
 
def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"sending order {order_type} - {side} {quantity} {symbol}")
        params={'quoteOrderQty':50,}
        balance = client.get_asset_balance(asset='USDT')
        
        amount = None
        price = None
        #order = client.create_order(symbol=symbol, side=side, type=order_type,quoteOrderQty=50)
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return order
	


		
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    #print(request.data)
    data = json.loads(request.data)
    
    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }

    side = data['strategy']['order_action'].upper()
    quantity = data['strategy']['order_contracts']
    parite=data['ticker']
    print(parite)
	#orderplace("DOGEUSD",5)
    order_response = order(side, quantity, parite)

    if order_response:
        return {
            "code": "success",
            "message": "order executed"
        }
    else:
        print("order failed")

        return {
            "code": "error",
            "message": "order failed"
        }