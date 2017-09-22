from flask import Flask, Response
from core import chain, genesis_block, wallet

import json

def render_response(msg, mimetype='application/json', code=200):
  # application/json text/html
  if mimetype == 'application/json':
    msg = json.dumps(msg)

  resp = Response(msg, mimetype=mimetype)
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp, code

# print(helpers)
# maybe break this up so it loads core module instead of classes

main = Flask(__name__)

block_chain = chain()
# wallet = wallet()

# Eventually remove
genesis = genesis_block()
block_chain.append_block(genesis)
# block_chain.create_block({u'edit':0, u'html':'',u'data': { 'hello': 'world' }})

from server import root
from server.block import block
from server.wallet import wallet_route

main.register_blueprint(block, url_prefix='/block')
main.register_blueprint(wallet_route, url_prefix='/wallet')