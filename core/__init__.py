from core.block import block
from core.genesis_block import genesis_block
from core.chain import chain
from core.wallet import wallet
from core.node import node

class webchain(object):
  def __init__(self):
    self.block = block()
    self.genesis_block = genesis_block()
    self.chain = chain()
    self.wallet = wallet()
    self.node = node()

webchain = webchain()
print(webchain.node.__dict__)
print(webchain.node.get_local_ip())
print(webchain.node.get_external_ip())
webchain.chain.append_block(webchain.genesis_block)

