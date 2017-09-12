from core import block

class genesis_block(block):

  def __init__(self):
    super(genesis_block, self).__init__()

    self.parent_hash = 0
    self.index = 0
    self.data = {
      u'edit': 0,
      u'html': '<html><head><title>Hello World</title></head><body>Hello World</body></html>',
      u'data': { u'string': 'hello world' }
    }
    self.timestamp = 1505253995
    self.hash = 'e7e9ea934ea51d271cde20166b122a20e1fbd0bd2fb2c3bdaf8b44f29a9907ee'
