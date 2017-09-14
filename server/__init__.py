from flask import Flask
from core import chain, genesis_block

main = Flask(__name__)

block_chain = chain()
# Eventually remove
genesis = genesis_block()
block_chain = chain()
block_chain.append_block(genesis)
block_chain.create_block({u'edit':0, u'html':'',u'data': { 'hello': 'world' }})

from server import root
from server.block import block

main.register_blueprint(block, url_prefix='/block',hi='ho')