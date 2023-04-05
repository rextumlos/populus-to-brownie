from brownie import SimpleVoting, accounts


def deploy_simple_voting():
    voting = SimpleVoting.deploy([b'Messi', b'Ronaldo'], {'from': accounts[0]})
    return voting

def main():
    deploy_simple_voting()