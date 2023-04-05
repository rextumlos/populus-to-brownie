from brownie import accounts
from scripts.deploy import deploy_greeter


def test_greeter():
    greeter = deploy_greeter()
    greeting = greeter.greet()
    print(greeting)
    assert greeting == 'Hello'
    
def test_custom_greeting():
    account = accounts[0]
    greeter = deploy_greeter()
    
    expected = "Guten Tag"
    
    tx = greeter.setGreeting(expected, {"from": account})
    tx.wait(1)
    
    print(greeter.greet())
    assert greeter.greet() == expected