from web3 import Web3 

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/d56b20c82b3c4b50a963365334ee401c"))

dict = vars(web3.eth.getBlock('latest'))

print(dict.keys())


for i in dict.keys():
    print(i, dict[i], sep=' => ')