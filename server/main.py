from server import server
from flask import request, Response, json

import json

@server.route('/')
def index():
  return render_response({'hi':'hello world'})

# HELPER FUNCTIONS #############################################################

def render_response(msg, mimetype='application/json', code=200):
  # application/json text/html
  if mimetype == 'application/json':
    msg = json.dumps(msg)

  resp = Response(msg, mimetype=mimetype)
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp, code
