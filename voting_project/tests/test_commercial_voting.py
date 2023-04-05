import pytest
from brownie import CommercialVoting, accounts, web3
from brownie.exceptions import VirtualMachineError


@pytest.fixture()
def voting():
    voting = accounts[0].deploy(CommercialVoting, [b'Messi', b'Ronaldo'])
    return voting

def test_initial_state(voting):
    assert voting.manager() == accounts[0]
    
def test_vote_with_money(voting):
    account2 = accounts[1]
    account3 = accounts[2]
    
    tx = voting.vote(0, {'from': account2, 'value': web3.toWei('0.05', 'ether')})
    tx.wait(1)
    
    tx = voting.vote(1, {'from': account3, 'value': web3.toWei('0.15', 'ether')})
    tx.wait(1)
    
    assert web3.eth.get_balance(voting.address) == web3.toWei('0.2', 'ether')
    
def test_vote_with_not_enough_money(voting):
    account2 = accounts[1]
    
    with pytest.raises(VirtualMachineError):
        voting.vote(0, {'from': account2, 'value': web3.toWei('0.005', 'ether')})
        
def test_manager_account_could_withdraw_money(voting):
    account2 = accounts[1]
    
    tx = voting.vote(0, {'from': account2, 'value': web3.toWei('1', 'ether')})
    tx.wait(1)
    
    initial_balance = web3.eth.get_balance(str(accounts[0]))
    tx = voting.withdraw_money({'from': accounts[0]})
    tx.wait(1)
    after_withdraw_balance = web3.eth.get_balance(str(accounts[0]))
    
    assert abs((after_withdraw_balance - initial_balance) - web3.toWei('1', 'ether')) < web3.toWei('10', 'gwei')