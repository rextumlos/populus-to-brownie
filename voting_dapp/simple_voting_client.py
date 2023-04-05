import json
import time

from web3 import HTTPProvider, Web3

w3 = Web3(HTTPProvider("http://localhost:7545"))
w3.eth.default_account = '0x6Ca3DA6a23c7Aba8b8BB9deBcd0571D76D5E5a72'

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

nonce = w3.eth.getTransactionCount(Web3.toChecksumAddress(w3.eth.default_account))

txn = voting.functions.vote(0).buildTransaction({
    'gas': 70000,
    'gasPrice': w3.toWei('1', 'gwei'),
    'nonce': nonce
})

private_key = '0xb3012f159e2d1ad9a30281f02ad79211661c69181437cba3d8090299c1106dbf'
signed = w3.eth.account.signTransaction(txn, private_key=private_key)
w3.eth.sendRawTransaction(signed.rawTransaction)