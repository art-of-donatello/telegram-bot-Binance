#!/usr/bin/env python
# coding: utf-8

# In[32]:


import json, config
from flask import Flask, request, jsonify, render_template
from binance.client import Client
from binance.enums import *
import pandas as pd
from binance.helpers import round_step_size
from telethon import TelegramClient, events, sync

# In[33]:


client = Client(config.API_KEY, config.API_SECRET)

api_id = config.API_ID
api_hash = config.API_HASH
client = TelegramClient('anon', api_id, api_hash)

# In[34]:


def paritebul(data1):
    for data in data1:
        if data.find("$")>-1:
            parite=data.replace("$","")
            #print(parite)
    return parite

def pozisyonbul(data):
    buy=data.find("New signal available")
    sell=data.find("closed with")
    if buy>-1:
        return "buy"
    elif sell>-1:
        return "sell"
    else:
        return "error"

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

    
def quantitycalc(order,total):
    info=client.get_symbol_info(order)
    avg_price = client.get_avg_price(symbol=order)
    f = [i["stepSize"] for i in info["filters"] if i["filterType"] == "LOT_SIZE"][0]
    print(avg_price['price'])
    amount = total/float(avg_price['price'])
    precision = 5
    amt_str = "{:0.0{}f}".format(amount, precision)
    amt_str = rounded_amount = round_step_size(amount, float(f))
    return amt_str
   

def defmes(message):
	total=config.TOTAL    
   

	a_string = message
	first_word = a_string.split()[1]

	symbol=paritebul(a_string.split()) #pair is found here
	print(symbol)

	side=pozisyonbul(a_string)  #operation is found here

	print(side)

	quantity=quantitycalc(symbol,total) #Quantity calculated here


	mk_op=order(side,quantity,symbol)

	print(mk_op)


@client.on(events.NewMessage(chats='Signalscryptoglobal'))
async def my_event_handler(event):
	print(event.raw_text) 
	defmes(event.raw_text)

#client.start()
print("Started")
#client.run_until_disconnected()
     


# In[ ]:




