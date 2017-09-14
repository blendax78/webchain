from server import main, block_chain

from flask import request, Response
import json

@main.route('/')
def index():
  return render_response(block_chain.get_simple())

# HELPER FUNCTIONS #############################################################

def render_response(msg, mimetype='application/json', code=200):
  # application/json text/html
  if mimetype == 'application/json':
    msg = json.dumps(msg)

  resp = Response(msg, mimetype=mimetype)
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp, code
