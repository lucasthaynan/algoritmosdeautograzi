import datetime
import os
import gspread
import requests
from flask import Flask, request
from oauth2client.service_account import ServiceAccountCredentials
from tchan import ChannelScraper
from scraper import coleta

# TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
# TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
# GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
# GOOGLE_SHEETS_KEY = os.environ["GOOGLE_SHEETS_KEY"] 
# with open("credenciais.json", mode="w") as arquivo:
#   arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
# conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
# api = gspread.authorize(conta)
# planilha = api.open_by_key(GOOGLE_SHEETS_KEY)
# sheet = planilha.worksheet("Página1")
app = Flask(__name__)



@app.route("/")
def index():
  return menu + "Olá, mundo! Esse é meu site. (Graziela França)"

           
           
           


