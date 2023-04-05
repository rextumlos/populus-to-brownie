import json
import time

from web3 import HTTPProvider, Web3

w3 = Web3(HTTPProvider("http://localhost:7545"))

print(w3.eth.coinbase)
print(w3.eth.get_balance(w3.eth.coinbase))

# Change this address to your smart contract address
address = "0x5Bc86b19E6D720e9fA14044dDbcc210082627a1e"
false = False
true = True

abi_dir = '../voting_project/build/contracts/SimpleVoting.json'
with open(abi_dir, 'r') as f:
    data = json.load(f)
    
abi = data['abi']

voting = w3.eth.contract(address = address, abi = abi)

event_filter = voting.events.Voting.createFilter(fromBlock=1)

while True:
    print(event_filter.get_new_entries())
    time.sleep(2)