import pytest
from brownie import Greeter2, accounts, web3
from brownie.exceptions import VirtualMachineError

# from scripts.deploy_greeter2 import deploy_greeter2


# Greeter 2 test
@pytest.fixture()
def greeter2_contract():
    return accounts[0].deploy(Greeter2, 'Hola')

def test_greeter2(greeter2_contract):
    greeting2 = greeter2_contract.greet()
    assert greeting2 == 'Hola'