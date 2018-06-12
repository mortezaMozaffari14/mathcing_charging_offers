import helpers
import constants
import sha3

class Transaction:
    def __init__(self, _arrival_time, counter):
        self.arrival_time = _arrival_time
        self.agent, self.tip1, self.tip2 = None, None, None

        #Give transaction a random hash as identifier? For now just using numbers
        self.id = counter
        #self.id = sha3.keccak_256(self.arrival_time).hexdigest()

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)


