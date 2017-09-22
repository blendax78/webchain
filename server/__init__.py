from flask import Flask, Response
from core import webchain

import json

def render_response(msg, mimetype='application/json', code=200):
  # application/json text/html
  if mimetype == 'application/json':
    msg = json.dumps(msg)

  resp = Response(msg, mimetype=mimetype)
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp, code

main = Flask(__name__)

from server import root
from server.block import block
from server.wallet import wallet

main.register_blueprint(block, url_prefix='/block')
main.register_blueprint(wallet, url_prefix='/wallet')