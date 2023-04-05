from brownie import Greeter2, accounts


def deploy_greeter2():
    greeter2 = Greeter2.deploy('Hola', {'from': accounts[0]})
    return greeter2

def main():
    deploy_greeter2()