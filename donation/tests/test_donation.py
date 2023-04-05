import time

import pytest
from brownie import accounts, web3
from brownie.exceptions import VirtualMachineError
from scripts.deploy_donation import deploy_donation


def test_donatee():
    Donation = deploy_donation()
    donatee = Donation.donatee()
    
    expected = accounts[0]
    
    assert donatee == expected
    
def test_donate_less_than_1_eth():
    Donation = deploy_donation()
    
    # instead of eth_tester
    with pytest.raises(VirtualMachineError):
        Donation.donate('Taylor Swift', {'from': accounts[0], 'value': web3.toWei('0.8', 'ether')})
        
def test_donate_1_eth():
    Donation = deploy_donation()
    account2 = accounts[1]
    
    donatur_name = 'Taylor Swift'
    tx = Donation.donate(donatur_name, {'from': account2, 'value': web3.toWei('1', 'ether')})
    tx.wait(1)
    
    donatur = Donation.donaturs(0)
    donation_sum = Donation.donatur_details(donatur)[0]
    donation_name = Donation.donatur_details(donatur)[1]
    donation_time = Donation.donatur_details(donatur)[2]
    
    assert donatur == account2
    assert donation_sum == web3.toWei('1', 'ether')
    assert donation_name == donatur_name
    assert (int(time.time() - donation_time)) < 600     # could be flaky
    
    assert web3.eth.get_balance(Donation.address) == web3.toWei('1', 'ether')
    
def test_other_account_could_not_withdraw_money():
    Donation = deploy_donation()
    account2 = accounts[1]
    
    donatur_name = "Taylor Swift"
    tx = Donation.donate(donatur_name, {'from': account2, 'value': web3.toWei('1', 'ether')})
    tx.wait(1)
    
    with pytest.raises(VirtualMachineError):
        Donation.withdraw_donation({'from': account2})
        
def test_manager_account_could_withdraw_money():
    Donation = deploy_donation()
    account2 = accounts[1]
    
    donatur_name = "Taylor Swift"
    tx = Donation.donate(donatur_name, {'from': account2, 'value': web3.toWei('1', 'ether')})
    tx.wait(1)
    
    initial_balance = web3.eth.get_balance(str(accounts[0]))
    tx = Donation.withdraw_donation({'from': accounts[0]})
    tx.wait(1)
    
    after_withdraw_balance = web3.eth.get_balance(str(accounts[0]))
    
    assert abs((after_withdraw_balance - initial_balance) - web3.toWei('1', 'ether')) < web3.toWei('10', 'gwei')