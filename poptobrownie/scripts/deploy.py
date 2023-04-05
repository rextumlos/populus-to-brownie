from brownie import Greeter, accounts


def deploy_greeter():
    account = accounts[0]
    greeter = Greeter.deploy({"from": account})
    return greeter

def main():
    deploy_greeter()