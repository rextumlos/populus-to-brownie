# Unit testing
# Works same with pytest
from brownie import SimpleStorage, accounts
from scripts.deploy import deploy_simple_storage


# all methods should have "test" at the start of method name
# To run single method, brownie test -k method
# To play around with the failed test, brownie test --pdb
# check more flags in test using, brownie test --help
def test_can_set_number():
    # Arrange
    account = accounts[0]
    expected = 777
    simple_storage = deploy_simple_storage()
    # simple_storage = SimpleStorage.deploy({"from": account})
    
    # Act
    tx = simple_storage.setNumber(expected, {"from": account})
    tx.wait(1)
    
    # Assert
    assert simple_storage.num() == expected
    
    