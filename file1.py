# Chapter 6 - EX 6.2.5
class GreetingCard:
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print("Sender:", self._sender)
        print("Recipient:", self._recipient)
