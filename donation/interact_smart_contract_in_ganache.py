import json

from web3 import HTTPProvider, Web3

w3 = Web3(HTTPProvider("http://localhost:7545"))

print(w3.eth.coinbase)
print(w3.eth.get_balance(w3.eth.coinbase))

# Change this address to your smart contract address
address = "0xb13F61Fa9E18325Ea9AFE838394c09A327cC6f75"
false = False
true = True

abi_dir = './build/contracts/Donation.json'
with open(abi_dir, 'r') as f:
    data = json.load(f)
    
abi = data['abi']

donation = w3.eth.contract(address = address, abi = abi)
print(donation.functions.donatee().call())