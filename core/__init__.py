from core.block import block
from core.genesis_block import genesis_block
from core.chain import chain
from core.wallet import wallet

class webchain(object):
  def __init__(self):
    self.block = block()
    self.genesis_block = genesis_block()
    self.chain = chain()
    self.wallet = wallet()

webchain = webchain()
webchain.chain.append_block(webchain.genesis_block)

