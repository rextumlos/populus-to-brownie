from brownie import Donation, accounts


def deploy_donation():
    donation = Donation.deploy({"from": accounts[0]})
    return donation

def main():
    deploy_donation()
