from server import main, block_chain, render_response

from flask import request, Response
import json
# import server

@main.route('/')
def index():
  return render_response(block_chain.get_simple())

