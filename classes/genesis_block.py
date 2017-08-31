class genesis_block(object):

  def __init__(self):
    self.state = {u'Alice':50, u'Bob':50}
    self.transactions = [self.state]
    self.block_number = 0
    self.parent_hash = None
    self.txn_count = 1

  def get_state(self):
    return self.state

  def get_transactions(self):
    return self.transactions

  def get_contents(self):
    return {
      u'block_number': self.block_number,
      u'parent_hash': self.parent_hash,
      u'txn_count': self.txn_count,
      u'transactions': self.get_transactions()
    }
