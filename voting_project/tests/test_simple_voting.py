import pytest
from brownie import SimpleVoting, accounts
from brownie.exceptions import VirtualMachineError


@pytest.fixture()
def voting():
    voting = accounts[0].deploy(SimpleVoting, [b'Messi', b'Ronaldo'])
    return voting

def test_initial_state(voting):
    assert voting.proposals_count() == 2
    
    messi = voting.proposals(0)[0]
    ronaldo = voting.proposals(1)[0]
    
    assert len(messi) == 32
    assert bytes.fromhex(messi.hex()[24:]).lstrip(b'\x00') == b'Messi'
    assert bytes.fromhex(ronaldo.hex()[24:]).lstrip(b'\x00') == b'Ronaldo'
    assert voting.proposals(0)[1] == 0
    assert voting.proposals(1)[1] == 0
    
def test_vote(voting):
    account2 = accounts[1]
    
    # proposal1 vote_count
    assert voting.proposals(0)[1] == 0
    
    tx = voting.vote(0, {'from': account2})
    tx.wait(1)
    
    assert voting.proposals(0)[1] == 1
    
def test_fail_duplicate_vote(voting):
    account2 = accounts[1]
    
    tx = voting.vote(0, {'from': account2})
    tx.wait(1)
    
    with pytest.raises(VirtualMachineError):
        voting.vote(1, {'from': account2})
        
    with pytest.raises(VirtualMachineError):
        voting.vote(0, {'from': account2})
        
def test_winning_proposal(voting):
    account2 = accounts[1]
    account3 = accounts[2]
    account4 = accounts[3]
    
    tx = voting.vote(0, {'from': account2})
    tx.wait(1)
    
    tx = voting.vote(0, {'from': account3})
    tx.wait(1)
    
    tx = voting.vote(1, {'from': account4})
    tx.wait(1)
    
    winner_name = voting.winner_name()
    
    assert voting.proposals(0)[1] == 2
    assert voting.proposals(1)[1] == 1
    assert bytes.fromhex(winner_name.hex()[24:]).lstrip(b'\x00') == b'Messi'