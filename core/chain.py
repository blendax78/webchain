from core import block

class chain(object):

  def __init__(self):
    self.data = []

  def get_simple(self):
    blocks = []
    for block in self.data:
      blocks.append(block.get())

    return blocks

  def get_block(self, hash):
    block = [block for block in self.data if block.hash == hash] 
    return block[0] if len(block) > 0 else None
    # return next(block for block in self.get_json() if block['hash'] == hash)

  def append_block(self, block):
    # This will handle adding blocks in order according to hash
    # **eventually
    self.data.append(block)

  def create_block(self, data):
    parent = self.data[-1] # last block

    new_block = block(parent.index, parent.hash, data)
    self.append_block(new_block)

    return new_block

