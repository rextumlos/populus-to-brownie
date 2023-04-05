# @version 0.2.16

struct DonaturDetail:
    sum: uint256
    name: String[100]
    time: uint256

interface Hello:
    def say_hello() -> String[32]: view

# donatur_details: public(map(address, DonaturDetail))
donatur_details: public(HashMap[address, DonaturDetail])

donaturs: public(address[10])

donatee: public(address)

index: int128

@external
def __init__():
    self.donatee = msg.sender

@payable
@external
def donate(name: String[100]):
    assert msg.value >= as_wei_value(1, "ether")
    assert self.index < 10

    self.donatur_details[msg.sender] = DonaturDetail({
                                         sum: msg.value,
                                         name: name,
                                         time: block.timestamp
                                       })

    self.donaturs[self.index] = msg.sender
    self.index += 1

@external
def withdraw_donation():
    assert msg.sender == self.donatee

    send(self.donatee, self.balance)

@external
@view
def donation_smart_contract_call_hello_smart_contract_method(smart_contract_address: address) -> String[32]:
    return Hello(smart_contract_address).say_hello()
