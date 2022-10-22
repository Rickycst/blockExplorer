from web3 import Web3 

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/d56b20c82b3c4b50a963365334ee401c"))


class eth:

    
    def get_block(self, id):
        return vars(web3.eth.getBlock(int(id)))