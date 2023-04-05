from brownie import TokenBasedVoting, accounts


def deploy_token_based_voting():
    voting = TokenBasedVoting.deploy([b'Messi', b'Ronaldo'], {'from': accounts[0]})
    return voting

def main():
    deploy_token_based_voting()