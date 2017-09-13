# from server import main
# from core import chain, block, genesis_block
from server import block
from flask import request, Response, Blueprint, redirect
import json

block = Blueprint('block', __name__)

# Registered with a url_prefix='/block'

@block.route('/', methods=['POST'])
def create_block():
  return render_response({'test':'yo'})

@block.route('/', methods=['GET'])
def redirect_home():
  return redirect('http://localhost:5001/')

# HELPER FUNCTIONS #############################################################

def render_response(msg, mimetype='application/json', code=200):
  # application/json text/html
  if mimetype == 'application/json':
    msg = json.dumps(msg)

  resp = Response(msg, mimetype=mimetype)
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp, code
