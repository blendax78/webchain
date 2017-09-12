from core import block

class chain(object):

  def __init__(self):
    self.data = []

  def get_json(self):
    blocks = []
    for block in self.data:
      blocks.append(block.get())

    return blocks

  def append_block(self, block):
    # This will handle adding blocks in order according to hash
    # **eventually
    self.data.append(block)

  def create_block(self, data):
    parent = self.data[-1] # last block

    new_block = block(parent.index, parent.hash, data)
    self.append_block(new_block)

    return new_block

    # parent_block = 
# def makeBlock(txns,chain):
#   print('chain===')
#   print(chain)
#   parentBlock = chain[-1]
#   print(parentBlock)
#   parent_hash  = parentBlock[u'hash']
#   index = parentBlock[u'contents'][u'index'] + 1
#   txnCount    = len(txns)
#   blockContents = {u'index':index,u'parent_hash':parent_hash,
#                    'txns':txns}
#   blockHash = hashMe( blockContents )
#   block = {u'hash':blockHash,u'contents':blockContents}

#   return block
