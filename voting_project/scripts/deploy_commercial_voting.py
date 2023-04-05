from brownie import CommercialVoting, accounts


def deploy_commercial_voting():
    voting = CommercialVoting.deploy([b'Messi', b'Ronaldo'], {'from': accounts[0]})
    return voting

def main():
    deploy_commercial_voting()