from server import main, block_chain, render_response, webchain

from flask import request, Response
import json
# import server

@main.route('/')
def index():
  return render_response(webchain.chain.get_simple())

