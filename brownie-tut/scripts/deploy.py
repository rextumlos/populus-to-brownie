from brownie import SimpleStorage, accounts


def deploy_simple_storage():
    account = accounts[0]
    simple_storage_contract = SimpleStorage.deploy({"from": account})
    print("Contract Address:", simple_storage_contract.address)
    return simple_storage_contract
    

def main():
    deploy_simple_storage()