import hashlib
import json
import sys

from core import genesis_block
from core import chain

genesis = genesis_block()
block_chain = chain()
block_chain.append_block(genesis)
new = block_chain.create_block({u'edit':0, u'html':'',u'data': {}})

# TODO:
# Remove notion of transactions
# Save chain to disk


#3
txnBuffer = [{ u'edit': 0,
    u'html': '<html><head><title>Hello World</title></head><body>Hello World</body></html>',
    u'data': { u'string': 'hello world' }
  } for i in range(30)]

#4
def updateState(txn, state):
  # Inputs: txn, state: dictionaries keyed with account names, holding numeric values for transfer amount (txn) or account balance (state)
  # Returns: Updated state, with additional users added to state if necessary
  # NOTE: This does not not validate the transaction- just updates the state!

  # If the transaction is valid, then update the state
  state = state.copy() # As dictionaries are mutable, let's avoid any confusion by creating a working copy of the data.
  # for key in txn:
  #   if key in state.keys():
  #     state[key] += txn[key]
  #   else:
  #     state[key] = txn[key]
  return state

#5
def isValidTxn(txn,state):
  # Assume that the transaction is a dictionary keyed by account names

  # Check that the sum of the deposits and withdrawals is 0
  if txn['edit'] < 0:
    return False
  # if sum(txn.values()) is not 0:
  #     return False

  # Check that the transaction does not cause an overdraft
  # for key in txn.keys():
  #   if key in state.keys():
  #     acctBalance = state[key]
  #   else:
  #     acctBalance = 0
  #   if (acctBalance + txn[key]) < 0:
  #     return False

  return True

#7
state = genesis.data  # Define the initial state

#8
chain = [genesis.get()]


#14
def checkBlockHash(block):
  # Raise an exception if the hash does not match the block contents
  # expectedHash = hashMe( block['contents'] )
  # if block['hash']!=expectedHash:
  #   raise Exception('Hash does not match contents of block %s'%
  #                   block['contents']['index'])
  return

#15
def checkBlockValidity(block,parent,state):
  # We want to check the following conditions:
  # - Each of the transactions are valid updates to the system state
  # - Block hash is valid for the block contents
  # - Block number increments the parent block number by 1
  # - Accurately references the parent block's hash
  parentNumber = parent['index']
  parent_hash   = parent['hash']
  index  = block['index']

  # Check transaction validity; throw an error if an invalid transaction was found.
  for txn in block['txns']:
    if isValidTxn(txn,state):
      state = updateState(txn,state)
    else:
      raise Exception('Invalid transaction in block %s: %s'%(index,txn))

  checkBlockHash(block) # Check hash integrity; raises error if inaccurate

  if index!=(parentNumber+1):
    raise Exception('Hash does not match contents of block %s'%index)

  if block['parent_hash'] != parent_hash:
    raise Exception('Parent hash not accurate at block %s'%index)

  return state

#16
def checkChain(chain):
  # Work through the chain from the genesis block (which gets special treatment),
  #  checking that all transactions are internally valid,
  #    that the transactions do not cause an overdraft,
  #    and that the blocks are linked by their hashes.
  # This returns the state as a dictionary of accounts and balances,
  #   or returns False if an error was detected


  ## Data input processing: Make sure that our chain is a list of dicts
  if type(chain)==str:
    try:
      chain = json.loads(chain)
      assert( type(chain)==list)
    except:  # This is a catch-all, admittedly crude
      return False
  elif type(chain)!=list:
    return False

  state = {}
  ## Prime the pump by checking the genesis block
  # We want to check the following conditions:
  # - Each of the transactions are valid updates to the system state
  # - Block hash is valid for the block contents

  for txn in chain[0]['transactions']:
    state = updateState(txn,state)

  checkBlockHash(chain[0])
  parent = chain[0]

  ## Checking subsequent blocks: These additionally need to check
  #    - the reference to the parent block's hash
  #    - the validity of the block number
  for block in chain[1:]:
    state = checkBlockValidity(block,parent,state)
    parent = block

  return state

#17
checkChain(chain)

#18
chainAsText = json.dumps(chain,sort_keys=True)
checkChain(chainAsText)

#19
import copy
nodeBchain = copy.copy(chain)


#20
print('===================================')
print('===================================')
print('Blockchain on Node A is currently %s blocks long' % len(block_chain.data))

try:
  print('New Block Received; checking validity...')
  state = checkBlockValidity(newBlock,chain[-1],state) # Update the state- this will throw an error if the block is invalid!
  chain.append(newBlock)
except:
  print('Invalid block; ignoring and waiting for the next block...')

print('Blockchain on Node A is now %s blocks long' % len(block_chain.data))
