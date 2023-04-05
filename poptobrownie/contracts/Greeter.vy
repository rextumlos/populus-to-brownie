# @version 0.2.16

greeting: String[20]

@external
def __init__():
    self.greeting = "Hello"

@external
def setGreeting(new_greet: String[20]):
    self.greeting = new_greet

@external
@view
def greet() -> String[20]:
    return self.greeting