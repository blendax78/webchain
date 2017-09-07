from core import block

class genesis_block(block):

  def __init__(self):
    self.state = {u'Alice':50, u'Bob':50}
    self.transactions = [self.state]
    self.block_number = 0
    self.parent_hash = None
    self.txn_count = 1

