import datetime
import os
import gspread
import requests
from flask import Flask, request
from oauth2client.service_account import ServiceAccountCredentials
from tchan import ChannelScraper

@app.route("/telegram-bot", methods=["POST"])
def telegram_bot():
  hoje = datetime.now().strftime('%d-%m-%Y')
  update-request.json
  chat_id=update['message']['chat']['id']
  message=update['message']['text']
  nova_mensagem={'chat_id':chat_id,'text':planilha}
  mensagem_if={'chat_id':chat_id,'text':f'Olá! Se quer receber as notícias de sites independentes do Nordeste me envie seu e-mail, por favor'}
  mensagem_else={'chat_id':chat_id,'text':f'Não entendi! Se quiser ter acesso às matérias de sites indepentes do Nordeste, envie seu e-mail, por favor'} 
  if message=='Olá':
    texto_resposta=requests.post(f"https://api.telegram.org./bot{token}/sendMessage", data=mensagem_if)                                      
  elif message.lower()=='sim':
    texto_resposta=requests.post(f"https://api.telegram.org./bot{token}/sendMessage", data=nova_mensagem)
  else:
    texto_respostas=requests.post(f"https://api.telegram.org./bot{token}/sendMessage", data=mensagem_else)                           
  return "ok"
