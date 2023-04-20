from card import Card
import random


class Deck:

    def __init__(self):
        suits = ["spades", "hearts", "clubs", "diamonds"]
        self.cards = []

        for s in suits:
            for i in range(2, 15):
                str_val = ""
                if i == 14:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(Card(s, i, str_val))

        self.shuffled_deck = self.shuffle()

    def show_cards(self):
        for card in self.shuffled_deck:
            card.card_info()
            # card.show()

    def shuffle(self):
        shuffled = []
        for i in range(len(self.cards)):
            rand = random.randint(0, len(self.cards)-1)
            shuffled.append(self.cards.pop(rand))
        self.cards = shuffled
        return shuffled

    def deal(self):
        return self.shuffled_deck.pop()


# print()
# test_deck = Deck()
# test_deck.show_cards()
# print()
# test_deck.shuffle()
# test_deck.show_cards()
# print()


# if __name__ == "__main__":
#     # create a deck
#     deck = Deck()
#     # shuffle the deck
#     print()
#     deck.shuffle()
#     # print all the cards in the deck
#     print()
#     deck.show_cards()
