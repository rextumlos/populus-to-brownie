import pytest
from brownie import TokenBasedVoting, accounts, web3
from brownie.exceptions import VirtualMachineError


@pytest.fixture()
def voting():
    voting = accounts[0].deploy(TokenBasedVoting, [b'Messi', b'Ronaldo'])
    return voting

def assign_tokens(voting):
    for i in range(1, 9):
        tx = voting.assign_token(accounts[i], {'from': accounts[0]})
        tx.wait(1)
        
def test_assign_token(voting):
    account2 = accounts[1]
    
    assert not voting.token(str(account2))
    
    tx = voting.assign_token(str(account2))
    tx.wait(1)
    
    assert voting.token(str(account2))
    
def test_cannot_vote_without_token(voting):
    account10 = accounts[9]
    assign_tokens(voting)
    
    with pytest.raises(VirtualMachineError):
        voting.vote(0, {'from': account10})
        
def test_can_vote_with_token(voting):
    account2 = accounts[1]
    
    assign_tokens(voting)
    # b'Messi' vote_count
    assert voting.proposals(0)[1] == 0
    
    tx = voting.vote(0, {'from': account2})
    tx.wait(1)
    
    assert voting.proposals(0)[1] == 1
    
