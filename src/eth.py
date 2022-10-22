from web3 import Web3 

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/d56b20c82b3c4b50a963365334ee401c"))


class eth:

    
    def get_block(self, id):
        return vars(web3.eth.getBlock(int(id)))

    def get_transaction(self, trx_hash):
        # 0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060
        return web3.eth.get_transaction(trx_hash)
