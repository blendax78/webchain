from flask import request, Response, Blueprint, redirect
import json
from server import wallet, render_response, webchain

wallet = Blueprint('wallet', __name__)

# Registered with a url_prefix='/wallet'
@wallet.route('/', methods=['POST'])
@wallet.route('', methods=['POST'])
def create_wallet():
  # Expects all params to be JSON encoded
  wallet = webchain.wallet.create()

  return render_response({'wallet': wallet.get()})


@wallet.route('/', methods=['GET'])
@wallet.route('', methods=['GET'])
def view_wallet():
  return render_response({'wallet': webchain.wallet.test()})
