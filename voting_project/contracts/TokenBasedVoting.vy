# @version 0.2.16

struct Proposal:
    name: bytes32
    vote_count: int128

proposals: public(HashMap[int128, Proposal])

token: public(HashMap[address, bool])
index: int128
maximum_token: int128
manager: public(address)

@external
def __init__(_proposalNames: bytes32[2]):
    for i in range(2):
        self.proposals[i] = Proposal({
            name: _proposalNames[i],
            vote_count: 0
        })
        self.index = 0
        self.maximum_token = 8
        self.manager = msg.sender

@external
def assign_token(target: address):
    assert msg.sender == self.manager
    assert self.index < self.maximum_token
    assert not self.token[target]
    self.token[target] = True
    self.index += 1

@external
def vote(proposal: int128):
    assert self.index == self.maximum_token
    assert self.token[msg.sender]
    assert proposal < 2 and proposal >= 0

    self.token[msg.sender] = False
    self.proposals[proposal].vote_count += 1


@view
@internal
def _winning_proposal() -> int128:
    winning_vote_count: int128 = 0
    winning_proposal: int128 = 0
    for i in range(2):
        if self.proposals[i].vote_count > winning_vote_count:
            winning_vote_count = self.proposals[i].vote_count
            winning_proposal = i

    return winning_proposal

@view
@external
def winner_name() -> bytes32:
    return self.proposals[self._winning_proposal()].name
