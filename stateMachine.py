'''state machine includes: State/Transition/Condition'''

#interface
class State:
    def open():
        pass
    def close():
        pass
    #All transition method is defined in State class. Just like abstract method.

#Then each specific state is corresponding to a specific class.
class OpenState(State):
    def open(self, door):
        print("Already opened.")
    def close(self, door):
        print("Door closed.")
        door.state = ClosedState()

class ClosedState(State):
    def open(self, door):
        print("Door opened.")
        door.state = OpenState()
    def close(self, door):
        print("Already closed.")
'''
In specific state class, we need to define instance method with two types of parameters: self-state and context state.
And the method in interface will be overriding accoding to the self-state.(transition)'''
#In state pattern, state is not a string, but a object(class).
class Door:
    def __init__(self):
        self.state = ClosedState()
    def open(self):
        self.state.open(self)
    def close(self):
        self.state.close(self)

door = Door()
door.open()
door.close()
door.close()
'''
Output:
Door opened.
Door closed.
Already closed.
'''
#A more pratical example:
class State:
    def pay():
        pass
    def ship():
        pass
    def deliver():
        pass
    def cancel():
        pass

class CreatedState(State):
    def pay(self, order):
        print("Order paid.")
        order.state = PaidState()
    
    def cancel(self, order):
        print("Order cancelled.")
        order.state = CancelledState()
    
class PaidState(State):
    def ship(self, order):
        print("Order shipped.")
        order.state = ShippedState()
    
    def cancel(self, order):
        print("Order cancelled.")
        order.state = CancelledState()

class ShippedState(State):
    def deliver(self, order):
        print("Order delivered.")
        order.state = DeliveredState()
    
    def cancel(self, order):
        print("Order cancelled.")
        order.state = CancelledState()

class DeliveredState(State):
    pass

class CancelledState():
    pass
    
class Order:
    def __init__(self):
        self.state = CreatedState()
    def pay(self):
        self.state.pay(self)
    def ship(self):
        self.state.ship(self)
    def deliver(self):
        self.state.deliver(self)
    def cancel(self):
        self.state.cancel(self)
        


