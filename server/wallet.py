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
  # importing class, not object
  wallet().test()

  render_response({'wallet':'si'})
