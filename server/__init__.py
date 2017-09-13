from flask import Flask

main = Flask(__name__)

from server import root
from server.block import block

main.register_blueprint(block, url_prefix='/block')