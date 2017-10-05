from server import main, render_response, webchain
from flask import request, Response
import json

@main.route('/')
def index():
  return render_response(webchain.chain.get_simple())

@main.route('/<hash>', methods=['GET'])
def show_page(hash):
  data = webchain.wallet.get()
  if data['wallet_address'] == '':
    webchain.wallet.create()
    data = webchain.wallet.get()
  # return render_response(data)
  return render_response('<html><body><h1>hello world</h1><h3>%s</h3></body></html>' % data['wallet_address'], 'text/html')
