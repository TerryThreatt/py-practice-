class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


c = Card("A", "hearts")
print(c)
print(c.suit)
