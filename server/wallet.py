from flask import request, Response, Blueprint, redirect
import json
from server import wallet, render_response, webchain

wallet = Blueprint('wallet', __name__)

# Registered with a url_prefix='/wallet'
# @wallet_route.route('/', methods=['POST'])
# @wallet_route.route('', methods=['POST'])
# def create_wallet():
#   # Expects all params to be JSON encoded
#   return server.render_response({'test':'ing'})


@wallet.route('/', methods=['GET'])
@wallet.route('', methods=['GET'])
def view_wallet():
  webchain.wallet.test()

  return render_response({'wallet': webchain.wallet.test()})
