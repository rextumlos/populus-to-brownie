# @version 0.2.16

struct Proposal:
    name: bytes32
    vote_count: int128

event Voting:
    _from: indexed(address)
    _proposal: int128

proposals: public(HashMap[int128, Proposal])

proposals_count: public(int128)
voters_voted: public(HashMap[address, int128])

@external
def __init__(_proposalNames: bytes32[2]):
    for i in range(2):
        self.proposals[i] = Proposal({
            name: _proposalNames[i],
            vote_count: 0
        })
        self.proposals_count += 1

@external
def vote(proposal: int128):
    assert self.voters_voted[msg.sender] == 0
    assert proposal < self.proposals_count

    self.voters_voted[msg.sender] = 1
    self.proposals[proposal].vote_count += 1

    log Voting(msg.sender, proposal)

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