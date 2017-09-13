from server import main
from core import chain, block, genesis_block
from flask import request, Response
import json

block_chain = chain()
# Eventually remove
genesis = genesis_block()
block_chain = chain()
block_chain.append_block(genesis)
new = block_chain.create_block({u'edit':0, u'html':'',u'data': { 'hello': 'world' }})
# /Eventually remove

@main.route('/')
def index():
  return render_response(block_chain.get_json())

# HELPER FUNCTIONS #############################################################

def render_response(msg, mimetype='application/json', code=200):
  # application/json text/html
  if mimetype == 'application/json':
    msg = json.dumps(msg)

  resp = Response(msg, mimetype=mimetype)
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp, code
