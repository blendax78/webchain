from core import block
import difflib

class genesis_block(block):

  def __init__(self):
    super(genesis_block, self).__init__()
    html = '<html><head><title>Hello World</title></head><body>Hello World</body></html>'

    self.parent_hash = 0
    self.index = 0
    self.data = {
      u'edit': 0,
      u'html': html,
      u'title': 'Genesis Block',
      u'data': { u'string': 'hello world' },
      u'transactions': [li for li in list(difflib.ndiff('', html)) if li[0] != ' ']
    }
    self.timestamp = 1505253995
    self.hash = self.calculate_hash()
