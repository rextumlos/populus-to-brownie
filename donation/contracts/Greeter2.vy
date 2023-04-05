# @version 0.2.16

greeting: String[20]

@external
def __init__(greeting_param: String[20]):
    self.greeting = greeting_param

@external
def set_greeting(new_greeting: String[20]):
    self.greeting = new_greeting

@external
@view
def greet() -> String[20]:
    return self.greeting