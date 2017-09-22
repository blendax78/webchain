from flask import request, Response, Blueprint, redirect
import json
from server import render_response, webchain

block = Blueprint('block', __name__)

# Registered with a url_prefix='/block'
@block.route('/', methods=['POST'])
@block.route('', methods=['POST'])
def create_block():
  # Expects all params to be JSON encoded
  try:
    data = { u'data': json.loads(request.form['data']), u'html': request.form['html']}
    new_block = webchain.chain.create_block(data)
    return render_response(new_block.get())
  except Exception as error:
    return render_response({u'error': True, u'msg': str(error)})
 

@block.route('/', methods=['GET'])
@block.route('', methods=['GET'])
@block.route('/<hash>', methods=['GET'])
def view_block(hash=None):
  if hash:
    block = webchain.chain.get_block(hash)
    return render_response(block.get() if block else {})
  else:
    return redirect('/')

