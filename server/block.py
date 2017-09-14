from flask import request, Response, Blueprint, redirect
import json
from server import block_chain

block = Blueprint('block', __name__)

# Registered with a url_prefix='/block'
@block.route('', methods=['POST'])
def create_block():
  return render_response(block_chain.get_simple())

@block.route('/', methods=['GET'])
@block.route('', methods=['GET'])
@block.route('/<hash>', methods=['GET'])
def view_block(hash=None):
  if hash:
    block = block_chain.get_block(hash)
    return render_response(block.get() if block else {})
  else:
    return redirect('/')

# HELPER FUNCTIONS #############################################################

def render_response(msg, mimetype='application/json', code=200):
  # application/json text/html
  if mimetype == 'application/json':
    msg = json.dumps(msg)

  resp = Response(msg, mimetype=mimetype)
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp, code
