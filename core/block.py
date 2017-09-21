import datetime
import hashlib
import json
import sys
import random

class block(object):

  def __init__(self, index=0, parent_hash=None, data={}):
    self.index = index
    self.data = data

    properties = {
      u'edit': 0,
      u'html': '',
      u'title': '',
      u'data': {},
      u'transactions': []
    }

    for prop in properties:
      if prop not in self.data:
        self.data[prop] = properties[prop]

    self.parent_hash = parent_hash
    self.timestamp = int(datetime.datetime.utcnow().timestamp())
    self.transactions = {'input': '', 'diff': []}
    self.hash = self.calculate_hash()

  def get(self):
    return self.__dict__
    # return {
    #   u'hash': self.hash,
    #   u'index': self.index,
    #   u'parent_hash': self.parent_hash,
    #   u'timestamp': self.timestamp,
    #   u'transactions': self.get_transactions(),
    #   u'data': self.data
    # }

  # def get_transactions(self):
    # return self.transactions

  def calculate_hash(self):
    random.seed(0)
    msg = {
      u'index': self.index,
      u'parent_hash': self.parent_hash,
      u'timestamp': self.timestamp,
      u'data': self.data,
      u'transactions': json.dumps(self.transactions)
    }

    if type(msg) != str:
      # If we don't sort keys, we can't guarantee repeatability!
      msg = json.dumps(msg, sort_keys=True)

    if sys.version_info.major == 2:
      return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
      return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
