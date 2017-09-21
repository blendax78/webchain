from flask import request, Response, Blueprint, redirect
import json
from server import wallet, render_response

wallet_route = Blueprint('wallet_route', __name__)

# Registered with a url_prefix='/wallet'
# @wallet_route.route('/', methods=['POST'])
# @wallet_route.route('', methods=['POST'])
# def create_wallet():
#   # Expects all params to be JSON encoded
#   return server.render_response({'test':'ing'})


@wallet_route.route('/', methods=['GET'])
@wallet_route.route('', methods=['GET'])
def view_wallet():
  wallet.test()

  render_response({'wallet':'si'})

# HELPER FUNCTIONS #############################################################

# def render_response(msg, mimetype='application/json', code=200):
#   # application/json text/html
#   if mimetype == 'application/json':
#     msg = json.dumps(msg)

#   resp = Response(msg, mimetype=mimetype)
#   resp.headers['Access-Control-Allow-Origin'] = '*'

#   return resp, code
