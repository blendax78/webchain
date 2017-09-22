from core.block import block
from core.genesis_block import genesis_block
from core.chain import chain
from core.wallet import wallet

webchain = type('',(object,),{})()
webchain.block = block()
webchain.genesis_block = genesis_block()
webchain.chain = chain()
webchain.wallet = wallet()

webchain.chain.append_block(webchain.genesis_block)

# from core.block import block
# from core.genesis_block import genesis_block
# from core.chain import chain
# from core.wallet import wallet

# block = block()
# genesis_block = genesis_block()
# block_chain = chain()
# wallet = wallet()

# need to redo this and core/cli funcs