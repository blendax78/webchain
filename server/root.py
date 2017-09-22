from server import main, render_response, webchain
from flask import request, Response
import json

@main.route('/')
def index():
  return render_response(webchain.chain.get_simple())

