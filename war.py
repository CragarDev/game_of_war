from deck import Deck
from os import system


# clear the screen

system('clear')


print()

# for the card game, lets do a game of war

# War
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down.
# users select a number between 1 and 100, the computer selects a number between 1 and 100, the user closest to the computer number gets delt to first.
# Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack.
# If the cards are the same rank, it is War. Each player turns up three cards face down and one card face up.
# The player with the higher cards takes both piles (six cards).
# If the turned-up cards are again the same rank, each player places another card face down and turns another card face up.
# The player with the higher card takes all 10 cards, and so on.
# Whoever wins the war takes all the cards from both players.
# The game ends when one player has won all the cards.


# player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.deal())

    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

# create the game class


class Game:

    game_counter = 0
    war_counter = 0

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.deck = Deck()
        self.player1_hand = []
        self.player2_hand = []

    # this would be a dealing function
    def deal_hands(self):

        for i in range(52):
            if i % 2 == 0:
                self.player1_hand.append(self.deck.deal())
            else:
                self.player2_hand.append(self.deck.deal())

        return self.player1_hand, self.player2_hand

    # show the hands
    def show_hands(self):
        print(self.player1.name + "'s hand:")
        self.player1.show_hand()
        print(self.player2.name + "'s hand:")
        self.player2.show_hand()

    # war function
    def war(self):
        print()
        print("%" * 50)
        print("%" * 40)
        print("%" * 30)
        print("-------   WAR!   -------")
        print("%" * 30)
        print("%" * 40)
        print("%" * 50)
        print()
        pot = []
        for i in range(3):
            pot.append(self.player1.discard())
            pot.append(self.player2.discard())

        print(f"{self.player1.name} card: ")
        self.player1.hand[-1].show()
        print()
        print(f"{self.player2.name} card: ")
        self.player2.hand[-1].show()
        print()

        print("%" * 50)
        print("%" * 40)
        print("%" * 30)
        if self.player1.hand[-1].point_val > self.player2.hand[-1].point_val:
            print(self.player1.name + " wins the war!")
            self.player1.hand.extend(pot)
        else:
            print(self.player2.name + " wins the war!")
            self.player2.hand.extend(pot)
        print("%" * 30)
        print("%" * 40)
        print("%" * 50)

        Game.war_counter += 1
        return

    def play(self):
        print("Welcome to War, let's begin...")
        print()
        print("Shuffling the deck...")
        print()
        print("Dealing the cards...")
        print()
        self.player1.hand, self.player2.hand = self.deal_hands()
        print()
        print("*" * 20)
        print(
            f"Start the Game! {self.player1.name} vs {self.player2.name}")
        print("*" * 20)
        print()
        while len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
            # self.show_hands()
            print()
            print("=" * 50)
            input("Press enter to flip a card.")
            print("=" * 50)
            print()
            print(
                f"{self.player1.name} card: ")
            self.player1.hand[-1].show()
            print()
            print(f"{self.player2.name} card: ")
            self.player2.hand[-1].show()
            print()

            if self.player1.hand[-1].point_val > self.player2.hand[-1].point_val:
                print(self.player1.name + " wins the round!")
                self.player1.hand.insert(0, self.player1.discard())
                self.player1.hand.insert(0, self.player2.discard())
            elif self.player1.hand[-1].point_val < self.player2.hand[-1].point_val:
                print(self.player2.name + " wins the round!")
                self.player2.hand.insert(0, self.player1.discard())
                self.player2.hand.insert(0, self.player2.discard())
            else:
                self.war()

            print()
            print("Current Score:")
            player1_hand_length = len(self.player1.hand)
            print(f"p1: {player1_hand_length}")
            player2_hand_length = len(self.player2.hand)
            print(f"p2: {player2_hand_length}")
            print()
            Game.game_counter += 1

        print()
        print("*" * 50)
        print()

        if len(self.player1.hand) > 0:
            print(self.player1.name + " wins the game!")
        else:
            print(self.player2.name + " wins the game!")

        print()
        print("*" * 50)
        print(f"Total number of hands played: {Game.game_counter}")
        print(f"Total number of wars: {Game.war_counter}")
        print()


# # create the players
player_one = input("Enter player 1 name: ")
if player_one == "":
    player_one = "Player 1"

player1 = Player(player_one)

player_two = input("Enter player 2 name: ")
if player_two == "":
    player_two = "Player 2"

player2 = Player(player_two)


# # create the game
game = Game(player1, player2)


# play the game
game.play()
print()
